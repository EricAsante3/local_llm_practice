from localLLM import extract_document_to_json 
import json

def write_to_file(filename, content):
    """Write content to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Output written to: {filename}")

def main():
    # Example 1: Invoice extraction
    invoice_text = """



EVERSSURCE (ftir $52,884.46

Statement Date: 07/03/24

Service Provided To:
BOMBARDIER AVIATION SERVICES

PO;5700044505 Line 1

Electric Usage History - Kilowatt Hours (kWh)

Current Charges for Electricity

kWh/Day Supply Delivery
on) $19,256.83 $9,153.55
300074

Cost of electricity from Cost to deliver electricity
2500-4 Se ee NEWENERGY from Eversource
2000

15004

1000

500

Nov Dec Jan Feb Mar Apr May Jun Jul $0

Nov Dee dan Feb Mar Apr May Jun Ju $5,684 $11,368 $17,052 $22,736 $28,420

Average Temperature q Aan 4
Your electric supplier is

CONSTELLATION NEWENERGY C&l
1001 LOUISIANA ST

STE 2300

HOUSTON TX 77002-5089
844-636-3749

1) On Peak [MM Off Peak

News For You

We use more energy to keep cool in the summer which means your bill may be higher. Learn how to use less energy while staying cool at
eversource.com/energy-saving-tips.

Remit Payment To: Eversource, PO Box 56002, Boston, MA 02205-6002

CE_240703PROD.TXT
Please make your check payable to Eversource and consider adding $1 for Operation Fuel.

, ~ You can also add $2 or $3 when paying your bill online. 100% of your tax-deductible donation
EV FE RS= U RC FE provides energy assistance grants. If mailing, please allow up to 5 business days to post.

Total Amount Due
Account Number: 5161 733 0139 aE VL $52,884.46
Non-residential and residential non-hardship customers may be y J

subject to a 1.00% late payment charge if the “Total Amount Due”
is not received by 07/31/24.

Amount Enclosed

Eversource
PO Box 56002
BOMBARDIER AVIATION SERVICES
BLDG 85-173 Boston, MA 02205-6002

BRADLEY INTERNATIONAL AIRPORT
WINDSOR LOCKS CT 06096

§161733013939 O0O526644b? 0030429479

EVERSSURCE

Account Number: 5161 733 0139
Customer name key: BOMB
Statement Date: 07/03/24

Service Provided To
BOMBARDIER AVIATION SERVICES

Sve Addr: 0 PERIMETER RD
WINDSOR LOCKS CT 06096
Serv Ref: 176582006

Bill Cycle: 02

Service from 06/03/24 - 07/03/24 30 Days
Next read date on or about: Aug 05, 2024
Meter Current Previous Current Reading
Number Read Read Usage Type
081145171 2835 2780 55 On Peak
081145171 8047 7910 137 Off Peak

Total Demand Use = 289.40 kW

55 X Meter Constant of 720 = 39600 Billed Usage
137 X Meter Constant of 720 = 98640 Billed Usage
Max Off-Peak Demand: 289.4 kW

Max On-Peak Demand: 275.8 kW

Monthly kWh Use - On Peak

Nov Dec Jan Feb Mar Apr May
29520 29520 30960 29520 29520 28800 29520
Jun Jul
30960 39600

Monthly kWh Use - Off Peak

Nov Dec Jan Feb Mar Apr May
78480 81360 95040 83520 90720 81360 83520
Jun Jul
88560 98640

Contact Information
Emergency: 800-286-2000
WWW.eversource.com

Pay by Phone: 888-783-6618
Customer Service: 888-783-6617

Total Amount Due

by 07/31/24 $52,884.46
Electric Account Summary
Amount Due On 07/02/24 $22,454.99
Last Payment Received $0.00
Balance Forward $22,454.99
Current Charges/Credits
Electric Supply Services $19,256.83
Delivery Services $9,153.55
Other Charges or Credits $2,019.09
Total Current Charges $30,429.47
Total Amount Due $52,884.46

Total Charges for Electricity

Supplier

CONSTELLATION NEWENERGY
Service Reference: 176582006
Allocated for 06/03/24 to 06/30/24

Supply 124416.00kWh X $0.13930 $17,331.15
Allocated for 06/30/24 to 07/03/24

Supply 13824.00kWh X $0.13930 $1,925.68
Subtotal Supplier Services $19,256.83
Delivery

(DISTRIBUTION RATE: 037)

Service Reference: 176582006

Allocated for 06/03/24 to 06/30/24

Prod/Trans Dmd Chrg 275.80KW X $5.94000 X 0.90000 $1,474.43
Transmission Peak 35640.00kWh X $0.03755 $1,338.28
Transmission Off-Peak 88776.00kWh X $0.00842 $747.49
Fixed Monthly Charge $270.0000 X 0.90000 $243.00
Local Delivery Improvements § 289.40KW X $1.33000 X 0.90000 $346.41
Local Delivery Demand Chrg 289.40KW X $8.69000 X 0.90000 $2,263.40
Revenue Decoupling Peak 35640.00kWh X $0.00080 $28.51
Revenue Decoupling Off-Peak 88776.00kWh X $0.00080 $71.02

CE_240703PROD.TXT

EVERSSURCE

Account Number: 5161 733 0139
Customer name key: BOMB
Statement Date: 07/03/24

Service Provided To
BOMBARDIER AVIATION SERVICES

Continued from previous page...

Supply Rate
Dollars / kWh
0.165
0.144
0.124
0.14
0.08
0.06
0.04-
0.02+

Nov Dec Jan Feb Mar Apr May Jun Jul

Demand Profile
Max. Demand
3005

250+
200+
150+
100+

50 5

04

Total Amount Due
by 07/31/24

Continued from previous page...

$52,884.46

Nov Dec Jan Feb Mar Apr May Jun Jul

Important Messages About Your Account
Because the billing period spans a change in the rates, your usage has been
calculated partly on the old rate and partly on the new rate.

Thank you for participating in the Online Bill and Payment Service.

Prod/Trans CTA Dmd Chrg 275.80KW X $-0.16000 X 0.90000 -$39.72
FMCC Charge Peak 35640.00kWh X $0.00596 $212.41
FMCC Charge Off-Peak 88776.00kWh X $0.00133 $118.07
Comb Public Benefit Chrg 124416.00kWh X $0.00730 $908.24
Allocated for 06/30/24 to 07/03/24

Prod/Trans Dmd Chrg 275.80KW X $4.91000 X 0.10000 $135.42
Transmission Peak 3960.00kWh X $0.03105 $122.96
Transmission Off-Peak 9864.00kWh X $0.00696 $68.65
Fixed Monthly Charge $270.0000 X 0.10000 $27.00
Local Delivery Improvements § 289.40KW X $2.15000 X 0.10000 $62.22
Local Delivery Demand Chrg 289.40KW X $8.69000 X 0.10000 $251.49
Revenue Decoupling Peak 3960.00kWh X $0.00195 $7.72
Revenue Decoupling Off-Peak 9864.00kWh X $0.00195 $19.23
Prod/Trans CTA Dmd Chrg 275.80KW X $0.13000 X 0.10000 $3.59
FMCC Charge Peak 3960.00kWh X $0.07930 $314.03
FMCC Charge Off-Peak 9864.00kWh X $0.01779 $175.48
Comb Public Benefit Chrg 13824.00kWh X $0.01839 $254.22
Subtotal Delivery Services $9,153.55
Total Cost of Electricity $28,410.38
Other Charges or Credits

Late Payment Charge Jul 03 $224.55
6.35% CT Sales Tax after Exemption of $150.00

CT Sales Tax Supplier $1,222.81
CT Sales Tax Delivery $571.73
Subtotal Other Charges or Credits $2,019.09
Total Current Charges $30,429.47

CE_240703PROD.TXT




    """
    
    electricity_bill_schema = {
    "type": "object",
    "properties": {
        "balance_forward": {"type": "number"},
        "billing_period_start_date": {"type": "string"},
        "billing_period_end_date": {"type": "string"},
        "kwh_usage_on_peak": {"type": "number"},
        "kwh_usage_off_peak": {"type": "number"},
        "kwh_usage_total": {"type": "number"},
        "total_demand_use_kw": {"type": "number"},
        "kva_usage": {"type": "number"},
        "power_factor": {"type": "number"},
        "supply_charges_kwh": {
            "type": "object",
            "additionalProperties": {"type": "number"}
        },
        "supply_charges_kw_kva": {
            "type": "object",
            "additionalProperties": {"type": "number"}
        },
        "delivery_charges_kwh": {
            "type": "object",
            "additionalProperties": {"type": "number"}
        },
        "delivery_charges_kw_kva": {
            "type": "object",
            "additionalProperties": {"type": "number"}
        },
        "sales_tax": {"type": "number"},
        "late_fees": {"type": "number"},
        "fixed_fees": {"type": "number"},
        "misc": {"type": "number"},
        "total_current_charges": {"type": "number"}
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