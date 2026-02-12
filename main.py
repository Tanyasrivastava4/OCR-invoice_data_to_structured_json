import os
import cv2
import numpy as np
import json
import pytesseract
import re
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pdf2image import convert_from_bytes

from ocr.tesseract_ocr import extract_text
from utils.text_cleaner import clean_ocr_text
from llm.qwen3_extractor import extract_structured_invoice


app = FastAPI()

# Helper function for in-memory OCR 
def extract_text_from_pil_image(pil_image):
    """
    Converts a PIL Image to OpenCV format and extracts text using pytesseract
    """
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return pytesseract.image_to_string(thresh)


# Currency Normalization Function
def normalize_amount_and_currency(data: dict):
    """
    Extract currency symbol from amount and convert to currency code.
    Remove symbol from amount.
    Default currency = INR
    """

    amount = data.get("amount")

    if not amount:
        data["currency"] = "INR"
        return data

    amount = amount.strip()

    currency_map = {
        "$": "USD",
        "₹": "INR",
        "€": "EUR",
        "£": "GBP"
    }

    detected_currency = "INR"  # default

    for symbol, code in currency_map.items():
        if symbol in amount:
            detected_currency = code
            amount = amount.replace(symbol, "").strip()
            break

    data["amount"] = amount
    data["currency"] = detected_currency

    return data


# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "API is running"}


# Main Invoice Extraction Endpoint
@app.post("/extract-invoice")
async def extract_invoice(file: UploadFile = File(...)):

    # Validate file type
    if not file.filename.lower().endswith((".pdf", ".png", ".jpg", ".jpeg")):
        return JSONResponse(
            status_code=415,
            content={
                "status": False,
                "error": "415 Unsupported Media Type [Only PDF or image files (PDF, PNG, JPG, JPEG) are allowed]"
            }
        )

    try:
        file_bytes = await file.read()

        # If PDF
        if file.filename.lower().endswith(".pdf"):

            pages = convert_from_bytes(file_bytes, dpi=300)
            full_text = ""

            for page in pages:
                raw_text = extract_text_from_pil_image(page)
                clean_text = clean_ocr_text(raw_text)
                full_text += clean_text + "\n"

        # If Image
        else:
            file_array = np.frombuffer(file_bytes, np.uint8)
            img = cv2.imdecode(file_array, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(
                gray, 127, 255,
                cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )[1]

            raw_text = pytesseract.image_to_string(thresh)
            full_text = clean_ocr_text(raw_text)

        # LLM Extraction (UNCHANGED)
        json_output = extract_structured_invoice(full_text)

        # Convert JSON string to dict
        structured_data = json.loads(json_output)

        # Apply Currency Normalization
        structured_data = normalize_amount_and_currency(structured_data)

       
        if not structured_data.get("invoice_date"):

           
            date_candidates = re.findall(
                r'\b\d{1,4}[/-]\d{1,2}[/-]\d{2,4}\b',
                full_text
            )

            valid_date = None


            date_formats = [
                "%d/%m/%Y",
                "%m/%d/%Y",
                "%Y-%m-%d",
                "%d-%m-%Y",
                "%m-%d-%Y",
                "%Y/%m/%d"
            ]

            for candidate in date_candidates:
                for fmt in date_formats:
                    try:
                        datetime.strptime(candidate, fmt)
                        valid_date = candidate
                        break
                    except:
                        continue
                if valid_date:
                    break

            if valid_date:
                structured_data["invoice_date"] = valid_date

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "data": structured_data
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



