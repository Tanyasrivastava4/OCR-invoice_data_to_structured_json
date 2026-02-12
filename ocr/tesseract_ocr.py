import cv2
import pytesseract

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 127, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return pytesseract.image_to_string(thresh)
