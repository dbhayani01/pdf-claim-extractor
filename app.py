import streamlit as st
import pandas as pd
from extractor.pdf_reader import extract_text_or_form
from extractor.parser import extract_fields
from models.database import SessionLocal, Claim
st.title("📄 Unified PDF Claim Data Extractor with DB Storage")
# Upload section
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_file:
   temp_file = "temp.pdf"
   with open(temp_file, "wb") as f:
       f.write(uploaded_file.read())
   # Extract data
   raw_data = extract_text_or_form(temp_file)
   structured_data = extract_fields(raw_data)
   # Show extracted data
   st.subheader("Extracted Data")
   st.json(structured_data)
   # Store in DB
   db = SessionLocal()
   claim = Claim(
       client_name=structured_data.get("client_name"),
       contact_name=structured_data.get("contact_name"),
       incident_details=structured_data.get("incident_details"),
       vehicle=structured_data.get("vehicle"),
       insured_name=structured_data.get("insured_name"),
       incident_description=structured_data.get("incident_description"),
       claim_type=structured_data.get("claim_type"),
   )
   db.add(claim)
   db.commit()
   db.close()
   st.success("✅ Data saved to SQLite database (claims.db)")
   # Display as table
   df = pd.DataFrame([structured_data])
   st.dataframe(df)
   # Download button
   csv = df.to_csv(index=False).encode("utf-8")
   st.download_button("Download CSV", csv, "claims.csv", "text/csv")
# Button to view DB contents
if st.button("📂 Show Database Data"):
   db = SessionLocal()
   claims = db.query(Claim).all()
   db.close()
   if claims:
       records = [
           {
               "id": c.id,
               "client_name": c.client_name,
               "contact_name": c.contact_name,
               "incident_details": c.incident_details,
               "vehicle": c.vehicle,
               "insured_name": c.insured_name,
               "incident_description": c.incident_description,
               "claim_type": c.claim_type,
           }
           for c in claims
       ]
       st.subheader("Database Records")
       st.dataframe(pd.DataFrame(records))
   else:
       st.info("ℹ️ Database is empty. Upload a PDF first.")