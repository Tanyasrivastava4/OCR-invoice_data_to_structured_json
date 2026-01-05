import os
from ocr.tesseract_ocr import extract_text
from utils.text_cleaner import clean_ocr_text
from llm.qwen3_extractor import extract_structured_invoice
from pdf2image import convert_from_path  # NEW

INPUT_DIR = "data/input_images"
OUTPUT_DIR = "data/output_json"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_image(image_path, output_name):
    
    raw_text = extract_text(image_path)
    clean_text = clean_ocr_text(raw_text)

    json_output = extract_structured_invoice(clean_text)

    out_path = os.path.join(OUTPUT_DIR, output_name + ".json")
    with open(out_path, "w") as f:
        f.write(json_output)

    print(f"Processed: {output_name}")


for file_name in os.listdir(INPUT_DIR):
    file_path = os.path.join(INPUT_DIR, file_name)
    base_name, ext = os.path.splitext(file_name)
    ext = ext.lower()

    # ✅ IMAGE FILES — SAME AS BEFORE
    if ext in (".png", ".jpg", ".jpeg"):
        process_image(file_path, base_name)

    # 🆕 PDF FILES — NEW LOGIC
    elif ext == ".pdf":
        print(f"Converting PDF: {file_name}")

        pages = convert_from_path(file_path, dpi=300)

        for i, page in enumerate(pages):
            image_name = f"{base_name}_page{i+1}"
            image_path = os.path.join(OUTPUT_DIR, image_name + ".png")

            page.save(image_path, "PNG")

            # Reuse SAME pipeline
            process_image(image_path, image_name)

    else:
        print(f"Skipping unsupported file: {file_name}")




#This one the successfull one
#import os
#from ocr.tesseract_ocr import extract_text
#from utils.text_cleaner import clean_ocr_text
#from llm.qwen3_extractor import extract_structured_invoice  
#
#INPUT_DIR = "data/input_images"
#OUTPUT_DIR = "data/output_json"
#
#os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#for img_file in os.listdir(INPUT_DIR):
#    if not img_file.lower().endswith((".png", ".jpg", ".jpeg")):
#        continue
#
#    img_path = os.path.join(INPUT_DIR, img_file)
#
#    raw_text = extract_text(img_path)
#    clean_text = clean_ocr_text(raw_text)
#
#    # Call the API-based LLM
#    json_output = extract_structured_invoice(clean_text)
#
#    out_path = os.path.join(
#        OUTPUT_DIR,
#        os.path.splitext(img_file)[0] + ".json"
#    )
#
#    with open(out_path, "w") as f:
#        f.write(json_output)
#
#    print(f"Processed: {img_file}")
#



#import os
#from ocr.tesseract_ocr import extract_text
#from utils.text_cleaner import clean_ocr_text
#from llm.phi3_extractor import extract_structured_invoice
#
#INPUT_DIR = "data/input_images"
#OUTPUT_DIR = "data/output_json"
#
#os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#for img_file in os.listdir(INPUT_DIR):
#    if not img_file.lower().endswith((".png", ".jpg", ".jpeg")):
#        continue
#
#    img_path = os.path.join(INPUT_DIR, img_file)
#
#    raw_text = extract_text(img_path)
#    clean_text = clean_ocr_text(raw_text)
#
#    json_output = extract_structured_invoice(clean_text)
#
#    out_path = os.path.join(
#        OUTPUT_DIR,
#        img_file.replace(".png", ".json")
#    )
#
#    with open(out_path, "w") as f:
#        f.write(json_output)
#
#    print(f"Processed: {img_file}")







#import os
#from ocr.tesseract_ocr import extract_text
#from utils.text_cleaner import clean_ocr_text
#from llm.qwen3_extractor import extract_structured_invoice  
#
#from pdf2image import convert_from_path  # NEW: PDF -> Image conversion
#
#INPUT_DIR = "data/input_images"
#OUTPUT_DIR = "data/output_json"
#os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#def process_image(img_path, output_name):
#    """Process a single image file: OCR -> clean text -> LLM -> JSON output."""
#    raw_text = extract_text(img_path)
#    clean_text = clean_ocr_text(raw_text)
#
#    json_output = extract_structured_invoice(clean_text)
#
#    out_path = os.path.join(OUTPUT_DIR, output_name + ".json")
#    with open(out_path, "w") as f:
#        f.write(json_output)
#    print(f"Processed: {img_path}")
#
## Loop through files
#for file_name in os.listdir(INPUT_DIR):
#    file_path = os.path.join(INPUT_DIR, file_name)
#    base_name, ext = os.path.splitext(file_name)
#
#    ext = ext.lower()
#    if ext in [".png", ".jpg", ".jpeg"]:
#        # Directly process images
#        process_image(file_path, base_name)
#
#    elif ext == ".pdf":
#        # Convert PDF to images
#        print(f"Converting PDF to images: {file_name}")
#        images = convert_from_path(file_path, dpi=300)
#        for i, image in enumerate(images):
#            img_path = os.path.join(OUTPUT_DIR, f"{base_name}_page{i+1}.png")
#            image.save(img_path, "PNG")
#            process_image(img_path, f"{base_name}_page{i+1}")
#
#    else:
#        print(f"Skipping unsupported file: {file_name}")
#