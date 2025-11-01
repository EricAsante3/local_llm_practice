"""
pdf_ocr.py
Performs high-accuracy OCR on a PDF file and outputs the extracted text.
Dependencies:
    pip install pytesseract pdf2image Pillow
Also requires Tesseract installed:
    macOS: brew install tesseract
    Ubuntu: sudo apt install tesseract-ocr
"""

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
import sys

def ocr_pdf(pdf_path: str, output_txt: str = "output.txt"):
    """
    Extract text from a PDF using OCR with Tesseract.
    Args:
        pdf_path: Path to the input PDF.
        output_txt: Path to save extracted text.
    """
    # Convert PDF to images (300 DPI for good accuracy)
    print(f"Converting {pdf_path} to images...")
    images = convert_from_path(pdf_path, dpi=300)

    all_text = []

    for i, img in enumerate(images):
        print(f"Processing page {i+1}/{len(images)}...")
        text = pytesseract.image_to_string(img, lang="eng")
        all_text.append(text)

    final_text = "\n".join(all_text)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(final_text)

    print(f"OCR completed. Text saved to {output_txt}")
    return final_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_ocr.py <path_to_pdf> [output_txt]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_txt = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

    ocr_pdf(pdf_path, output_txt)
