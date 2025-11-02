from localLLM import extract_document_to_json 
import json
import os

file_path = os.path.expanduser("~/Documents/Projects/local_llm/local_llm_practice")

with open(file_path + "/examples/Original1.txt", "r", encoding="utf-8") as f:
    text = f.read()

def write_to_file(filename, content):
    """Write content to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Output written to: {filename}")



def main():
    # Example 1: Invoice extraction
    invoice_text = text
    
    electricity_bill_schema = {
    "type": "object",
    "properties": {
        "balance_forward": {"type": ["number", "null"]},
        "billing_period_start_date": {"type": "string"},
        "billing_period_end_date": {"type": "string"},
        "kwh_usage_on_peak": {"type": ["number", "null"]},
        "kwh_usage_off_peak": {"type": ["number", "null"]},
        "kwh_usage_total": {"type": ["number", "null"]},
        "total_demand_use_kw": {"type": ["number", "null"]},
        "kva_usage": {"type": ["number", "null"]},
        "power_factor": {"type": ["number", "null"]},
        "supply_charges_kwh": {
            "type": "object",
            "additionalProperties": {"type": ["number", "null"]}
        },
        "supply_charges_kw_kva": {
            "type": "object",
            "additionalProperties": {"type": ["number", "null"]}
        },
        "delivery_charges_kwh": {
            "type": "object",
            "additionalProperties": {"type": ["number", "null"]}
        },
        "delivery_charges_kw_kva": {
            "type": "object",
            "additionalProperties": {"type": ["number", "null"]}
        },
        "sales_tax": {"type": ["number", "null"]},
        "late_fees": {"type": ["number", "null"]},
        "fixed_fees": {"type": ["number", "null"]},
        "misc": {"type": ["number", "null"]},
        "total_current_charges": {"type": ["number", "null"]}
    },
    "required": ["total_current_charges"]
    }   
    
    print("=== INVOICE EXTRACTION ===")
    invoice_result = extract_document_to_json(invoice_text, electricity_bill_schema)
    invoice_json = json.loads(invoice_result['choices'][0]['message']['content'])
    
    # Print to console
    print("Generated JSON:")
    print(json.dumps(invoice_json, indent=2))
    
    # Write to file
    write_to_file("invoice_output2.txt", json.dumps(invoice_json, indent=2))

if __name__ == "__main__":
    main()