from llama_cpp import Llama
import json
import os
file_path = os.path.expanduser("~/Documents/Projects/local_llm/local_llm_practice")

base_path = os.path.join("/media", "eric", "GASSS")
model_file = os.path.join(base_path, "models", "NuExtract-2.0-8B-Q8_0.gguf")

with open(file_path + "/examples/Original3.txt", "r", encoding="utf-8") as f:
    text_variable = f.read()

with open(file_path + "/examples/Truth3.json", "r", encoding="utf-8") as f:
    json_variable = json.load(f)

def extract_document_to_json(document_text, schema_definition):
    # Initialize the LLaMA model
    llm = Llama(
        model_path= model_file,
        chat_format="chatml",
        n_ctx=41000,
        n_gpu_layers = 12,
        verbose=False
    )

    # Define the prompt for document extraction
    messages = [
        {
            "role": "system",
            "content": f"""You are a document analysis assistant that extracts structured information from text and outputs valid JSON.

            
You will receive as input a text invoice that is read in natural reading order (left-right, top-bottom).

Your task is to:
1. Parse the input carefully.
2. Populate the required values using the input invoice text.

General tips:

- Do not include fixed charges in Supply or Delivery sections.
- When a charge has an allocated month range, format it as: "Charge Name (MM/DD/YY-MM/DD/YY)".
- Don't include Delivery or Supplier SubTotals.
- Include duplicates if the same charge appears multiple times.
- Check all relevant lines for months and values, especially for usage fields.
- If you are not confident in a particular field, or it is not present, set its value to None.

Additional guidance on how to extract fields:

balance_forward:
Previous balance carried over (if any).

billing_period_start_date:
Use format MM/DD/YYYY.

billing_period_end_date:
Use format MM/DD/YYYY.

kwh_usage_on_peak:
If a 'Monthly kWh Use - On Peak' section exists, use the value closest to the billing end date.
If not present, search the invoice for any value that reasonably represents On-Peak usage.

kwh_usage_off_peak:
If a 'Monthly kWh Use - Off Peak' section exists, use the value closest to the billing end date.
If not present, search the invoice for any value that reasonably represents Off-Peak usage.

kwh_usage_total:
If a 'Monthly kWh Use' or total usage section exists, use the value closest to the billing end date.
Otherwise, combine On-Peak and Off-Peak if available, or search for any value that reasonably represents total usage.

total_demand_use_kw:
Peak kW demand, if present.

kva_usage:
Peak kVA usage, if present.

power_factor:
Power factor percentage or decimal, if present.

supply_charges_kwh:
All Supply charges using kWh as the unit. Exclude fixed fees.

supply_charges_kw_kva:
All Supply charges using kW or kVA as the unit. Exclude fixed fees.

delivery_charges_kwh:
All Delivery charges using kWh as the unit. Exclude fixed fees.

delivery_charges_kw_kva:
All Delivery charges using kW or kVA as the unit. Exclude fixed fees.

sales_tax:
Typically labeled 'Sales Tax'.

late_fees:
Typically includes 'Late' and appears under 'Other Charges or Credits'.

fixed_fees:
Typically labeled 'Fixed' and may appear under 'Other Charges or Credits' or Delivery.

misc:
Any charges under 'Other Charges or Credits' not classified as sales tax, late fees, or fixed fees.

total_current_charges:
Total amount of current charges as stated on the bill.

'Balance Forward'
'Billing Period Start Date'(String) - Use format MM/DD/YYYY,
'Billing Period End Date' - Use format MM/DD/YYYY,
'kWh Usage (On-Peak)' - Under 'Monthly kWh Use - On Peak' choose the latest amount under that section with the month closest to the billing end date. Keep in mind it may contain more than one line of months. Only return the value
'kWh Usage (Off-Peak)' - Under 'Monthly kWh Use - Off Peak' choose the latest amount under that section with the month closest to the billing end date. Keep in mind it may contain more than one line of months. Only return the value
'kWh Usage Total' - Under 'Monthly kWh Use' choose the latest amount under that section with the month closest to the billing end date. If there is no section that matches perfectly add both On-Peak and Off-Peak kWh Usage. Only return the value.
'Total Demand Use (kW)',
'kVA Usage',
'Power Factor',
'Supply Charges (kWh)' - Return all charges under the Supply section that explicitly use kWh as the unit to calculate cost. Only return charges under the Supply section.
Exclude any charge that uses kW, kVA, or any other unit.
Return the results as nested JSON where each charge name is a key and its dollar amount is the value.
If there are duplicates names under this section list them along with all other charges
After listing all individual charges, include an additional key "Supply Charges (kWh) total" whose value is the sum of all listed amounts.
Return NONE if no charges are listed.

'Supply Charges (kW/kVA)' - Return all charges under the Supply section that explicitly use kW or kVA as the unit to calculate cost. Only return charges under the Supply section.
Exclude any charge that uses kWh or other units.
Return the results as nested JSON where each charge name is a key and its dollar amount is the value.
If there are duplicates names under this section list them along with all other charges
After listing all individual charges, include an additional key "Supply Charges (kW/kVA) total" whose value is the sum of all listed amounts.
Return NONE if no charges are listed.

'Delivery Charges (kWh)' — Return all charges under the Delivery section that explicitly use kWh as the unit to calculate cost. Only return charges under the Delivery section.
Exclude any charge that uses kW, kVA, or any other units or no units.
Return the results as nested JSON where each charge name is a key and its dollar amount is the value.
If there are duplicates names under this section list them along with all other charges
After listing all individual charges, include an additional key "Delivery Charges (kWh) total" whose value is the sum of all listed amounts.
Return NONE if no charges are listed.

'Delivery Charges (kW/kVA)' — Return all charges under the Delivery section that explicitly use kW or kVA as the unit to calculate cost. Only return charges under the Delivery section.
Exclude any charge that uses kWh or any other units or no units.
Return the results as nested JSON where each charge name is a key and its dollar amount is the value.
If there are duplicates names under this section list them along with all other charges
After listing all individual charges, include an additional key "Delivery Charges (kW/kVA) total" whose value is the sum of all listed amounts.
Return NONE if no charges are listed.

'Sales Tax'
'Late Fees' - Typically under 'other charges or credits'
'Fixed Fees' - Charges that include 'fixed' within it. Use the final amount in this line.
'Misc' - This should be any charges under 'Other Charges or Credits' section that isnt Sales Tax Late fees pr Fixed Fees
'Total Current Charges'
            

            
SCHEMA DEFINITION:
{json.dumps(schema_definition, indent=2)}

Here is a example:

Input Document
"{text_variable}"

Expected Output:
{json.dumps(json_variable, indent=2)}

RULES:
- Extract only the information present in the document
- If a field is not found, use null
- Output must be valid JSON matching the schema
- Be precise and accurate"""
        },
        {
            "role": "user",
            "content": f"Extract information from this document:\n\n{document_text}"
        }
    ]

    # Generate completion
    result = llm.create_chat_completion(
        messages=messages,
        response_format={
            "type": "json_object",
            "schema": schema_definition
        },
        temperature=0.1,
        max_tokens=2000
    )
    
    return result