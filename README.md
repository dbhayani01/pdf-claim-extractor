# 📄 PDF Claim Data Extractor

A Python-based application to **extract structured data (key-value pairs)** from PDF forms.  
Currently supports **text-based PDFs**, with planned support for scanned/image PDFs via OCR.  
Includes a **Streamlit UI** to upload files, preview results, and download as CSV/JSON.  

---

## ✨ Features
- Upload **PDF forms** and extract fields like *Customer Name, Branch Name, Claim Type*.
- Works for **text-based PDFs** (OCR planned for scanned/image PDFs).
- Configurable field extraction (easy to add new fields via regex patterns).
- Simple, clean **UI with Streamlit**.
- Export results as **CSV/JSON**.
- Designed for **scalability & testing**.

---

## 📂 Project Structure
```
pdf_extractor_app/
│── app.py                  # Streamlit UI
│── extractor/
│   ├── pdf_reader.py       # Extracts text from PDFs
│   ├── parser.py           # Regex-based field extractor
│   ├── config.py           # Configurable fields
│── models/
│   ├── database.py         # SQLite/SQLAlchemy 
│   ├── schemas.py          # Data schema (Pydantic/ORM) (optional)
│── tests/
│   ├── test_extraction.py  # Unit tests (optional)
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/dbhayani01/pdf-claim-extractor.git
cd pdf-claim-extractor
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

👉 *This setup is for text-based PDFs only.*  
OCR dependencies (`pytesseract`, `pdf2image`, `Pillow`) are commented out in `requirements.txt`.  

---

## ▶️ Usage

### Run the Streamlit app:
```bash
streamlit run app.py
```

1. Open the web UI in your browser (default: [http://localhost:8501](http://localhost:8501)).  
2. Upload a **PDF form**.  
3. Extracted fields will be displayed.  
4. Download results as **CSV**.

---

## 📊 Example

**Uploaded PDF (sample form):**
```
Customer Name: John Doe
Branch Name: Mumbai
Claim Type: Accident Claim
```

**Extracted JSON:**
```json
{
  "customer_name": "John Doe",
  "branch_name": "Mumbai",
  "claim_type": "Accident Claim"
}
```

**UI Screenshot:**  
*(Add a screenshot of Streamlit app here)*  

---

## ✅ Testing

Run unit tests with `pytest`:
```bash
pytest
```

---

## 🚀 Future Enhancements
- Add **OCR support** (Tesseract + pdf2image) for scanned PDFs.
- Improve extraction using **NLP/ML models** instead of regex.
- Store extracted data in **PostgreSQL** / **MongoDB**.
- Add an **admin dashboard** for analytics & reporting.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  

---
