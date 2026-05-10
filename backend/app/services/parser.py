from io import BytesIO
import os
import tempfile

import fitz
from PIL import Image
import pytesseract
from docx import Document


def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    text = ""
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text.strip()


def extract_text_from_image_bytes(file_bytes: bytes) -> str:
    image = Image.open(BytesIO(file_bytes)).convert("RGB")
    return pytesseract.image_to_string(image).strip()


def extract_text_from_docx_bytes(file_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    try:
        doc = Document(tmp_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text.strip()
    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass


def extract_text_from_file(filename: str, file_bytes: bytes) -> str:
    name = filename.lower()

    if name.endswith(".pdf"):
        return extract_text_from_pdf_bytes(file_bytes)

    if name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".webp"):
        return extract_text_from_image_bytes(file_bytes)

    if name.endswith(".docx"):
        return extract_text_from_docx_bytes(file_bytes)

    raise ValueError("Unsupported file type. Use PDF, image, or DOCX.")