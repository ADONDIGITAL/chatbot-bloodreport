# app/parser.py

from PyPDF2 import PdfReader

def extract_data_from_pdf(pdf_bytes):
    reader = PdfReader(pdf_bytes)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
