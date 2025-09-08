"""
Configuration file for extracting fields from PDFs.
Supports both text-based (regex) and AcroForm (form fields).
"""
# Regex patterns for text-based PDFs
TEXT_FIELDS_TO_EXTRACT = {
   "insured_name": r"Insured\s*Name[:\s]+(.*)",
   "incident_description": r"description of the incident\s*(.*)",
   "claim_type": r"Category of Loss\s*(.*)",
   "customer_name": r"CUSTOMER\s*NAME\s*",
   "contact_number": r"CONTACT\s*NUMBER\s*"
}
# Mapping for form-based PDFs (AcroForms)
FORM_FIELDS_MAPPING = {
   "client_name": "Text Field 401",
   "contact_name": "Text Field 403",
   "incident_details": "Text Field 416",
   "vehicle": "Text Field 419"
}