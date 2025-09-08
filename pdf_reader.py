import pdfplumber
from PyPDF2 import PdfReader
def extract_text_or_form(file_path: str):
   """Return form fields (dict) if AcroForm exists, otherwise return text (str)."""
   reader = PdfReader(file_path)
   # Try extracting form fields (AcroForm)
   fields = reader.get_fields()
   if fields:
       return {k: v.get('/V') for k, v in fields.items()}
   # Fallback: Extract text
   text = ""
   with pdfplumber.open(file_path) as pdf:
       for page in pdf.pages:
           text += page.extract_text() or ""
   return text