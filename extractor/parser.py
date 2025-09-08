import re
from extractor.config import TEXT_FIELDS_TO_EXTRACT, FORM_FIELDS_MAPPING
def extract_fields(data):
   """Extract structured fields from either form dict or raw text."""
   result = {}
   if isinstance(data, dict):  
       # AcroForm handling
       for key, form_field in FORM_FIELDS_MAPPING.items():
           result[key] = data.get(form_field, None)
   elif isinstance(data, str):  
       # Text-based handling
       for key, pattern in TEXT_FIELDS_TO_EXTRACT.items():
            match = re.search(pattern, data, re.IGNORECASE)
            # result[key] = match.group(1).strip() if match else None
            if match:
                if match.lastindex:
                    result[key] = match.group(1).strip()
                else:
                    result[key] = match.group(0).strip()
            else:
                result[key] = None
   return result
