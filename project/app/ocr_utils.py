import pytesseract
from PIL import Image
import re

def extract_text_from_image(image_path):
    """
    Ekstrak teks dari gambar menggunakan Tesseract OCR.
    """
    image = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(image)
    return ocr_result

def extract_total_amount(ocr_text):
    """
    Cari jumlah total pengeluaran dalam teks OCR.
    """
    match = re.search(r"(?i)(total|jumlah|amount)[:\s]*([\d,\.]+)", ocr_text)
    if match:
        return match.group(2)  # Ambil angka setelah kata yang cocok
    return None
