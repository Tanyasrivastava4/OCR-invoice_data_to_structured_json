PROMPT_TEMPLATE = """
You are an invoice information extraction system.

TASK:
Extract invoice information from the given text.

RULES:
- Do NOT guess any value
- Use ONLY the provided text
- If a value is missing, return null
- Output MUST be valid JSON
- Follow the schema EXACTLY
- If the invoice contains information that does not fit any schema field,
  store it under "extra_fields" using descriptive keys

FIELD MAPPING RULES:
- quantity may appear as: Qty, QTY, Quantity, Units, UM
- unit_price may appear as: Rate, Price, Unit Rate
- net_price may appear as: Net Price, Net Amount
- amount may appear as: Amount, Line Amount, Value
- vat_percent may appear as: VAT, VAT%, VAT(%)
- gst_rate may appear as: GST, GST%, CGST, SGST, IGST
- gross_value may appear as: Gross Amount, Gross Worth
- hsn_sac may appear as: HSN, SAC, HSN/SAC
- uom may appear as: Unit, Units, UM, UOM

Map all such variations to the schema fields.

SCHEMA:
{schema}

INVOICE TEXT:
\"\"\"
{text}
\"\"\"
"""




#this was the one(successfull)
#PROMPT_TEMPLATE = """
#You are an invoice information extraction system.
#
#TASK:
#Extract invoice information from the given text.
#
#RULES:
#- Do NOT guess any value
#- Use ONLY the provided text
#- If a value is missing, return null
#- Output MUST be valid JSON
#- Follow the schema EXACTLY
#- If the invoice contains information that does not fit any schema field,
#  store it under "extra_fields" using descriptive keys
#
#SCHEMA:
#{schema}
#
#INVOICE TEXT:
#\"\"\"
#{text}
#\"\"\"
#"""
