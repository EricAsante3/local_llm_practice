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
    DATE: October 15, 2023
    FROM: Tech Solutions Inc.
    123 Business Ave, San Francisco, CA 94105
    TO: ABC Corporation
    456 Corporate Blvd, New York, NY 10001
    
    ITEMS:
    - Laptop Computer: $1,200.00
    - Software License: $450.00
    - Technical Support: $300.00
    
    SUBTOTAL: $1,950.00
    TAX (8.5%): $165.75
    TOTAL: $2,115.75
    
    PAYMENT DUE: November 15, 2023
    TERMS: Net 30
    """
    
    invoice_schema = {
        "type": "object",
        "properties": {
            "invoice_number": {"type": "string"},
            "date": {"type": "string"},
            "from_company": {"type": "string"},
            "to_company": {"type": "string"},
            "subtotal": {"type": "number"},
            "tax": {"type": "number"},
            "total": {"type": "number"},
            "due_date": {"type": "string"},
            "payment_terms": {"type": "string"}
        },
        "required": ["invoice_number", "date", "total"]
    }
    
    print("=== INVOICE EXTRACTION ===")

    
    # Print to console
    print("Generated JSON:")
    
    # Write to file
    
    # Example 2: Resume extraction
    resume_text = """



Ethan M. Thomas
ethan.thomas@uconn.edu | (860)-213-6711 | linkedin.com/in/ethanthomas0 | https://github.com/ethant0123

EDUCATION

University of Connecticut Storrs, Connecticut

B.S. in Computer Science and Engineering Expected Graduation, May 2026
Oo GPA: 3.5

o Related Coursework: Data Structures & Object Oriented Programming, Systems Programming, Algorithms and Complexity,
Computer Architecture, Cybersecurity Lab, C++ Essentials, Intro to Computer and Network Security, Electrical Circuits

SKILLS

Programming Languages: Python, C/C++, SQL, HTML, CSS, JavaScript, R

Frameworks and Tools: React.js, Node.js, Next.js, Flask, Amazon Web Services (AWS), Docker, Selenium, Linux, Firebase, NumPy, Pandas, Jira
EXPERIENCE

JPMorgan Chase New York City, New York
Software Engineer Intern Jun 2025 — Aug 2025
e Contributed to the development of the Canadian dollar pricing application within Athena, JP Morgan’s proprietary trading and risk
management platform
e Engineered an alert system in Python to monitor pricing discrepancies between treasury bond data that traders and downstream
clients see by integrating a threshold-based visual alert mechanism, and embedded the system into existing Athena interfaces
e Refactored and uplifted cross currency pricing application dashboards by implementing dynamic resizability of widgets to enhance
and improve usability amongst traders using Enaml, a Python-based UI framework
Headstarter Al Remote
Software Engineering Fellow July 2024 — Sept 2024
e  =Built 5+ Al applications constructed with modern technologies like React, Next.js, OpenAl API, and more
e = Led 3+ engineering fellows in collaboration on projects, aiming to deploy and garner users for projects
e@ Mentored and coached by engineers from Amazon, Bloomberg, and Capital One, along with multiple startup founders
Pfizer Groton, Connecticut
Digital Client Partner Intern - R&D June 2024 — Aug 2024
e Built a custom tool that allows teams to automate checking whether any links on their SharePoint sites are broken using Python,
and optimized the efficiency of the tool by over 50% compared to the previous program
e Utilized Selenium to automate web scraping links off of pages and used Python’s urllib library to send HTTP requests to determine
whether links were broken or not
e = Created pipeline that automated writing data into Excel Spreadsheet, enabling easy access for tracking of link statuses
e  =Revitalized Central Request Manager form on SharePoint for PCRU Clinical Trials team using Microsoft Power Apps to provide
better organization of requests and streamline data into a SharePoint list
Pfizer Groton, Connecticut
Digital Client Partner Intern - Global Product Development June 2023 — Aug 2023
e@ Created a new process for requesting and assigning business analysts to projects that was approved by Pfizer’s Global Product
Development leadership team
e Wrote an easy to use, optimized Python script for converting CSV files to JSON files for a business operations team
PROJECTS

UConn Course Scheduler | Python, React, Tailwind, AWS(ECS, ECR, $3), Docker
e@ Developed a full-stack course scheduling web app helping over 80+ students to plan customized schedules for Fall 2025
e Built scalable backend services with Flask, constructing RESTful APIs to fetch and process data from UConn’s official database
e Engineered a responsive, modern UI with React and Tailwind CSS, providing intuitive scheduling functionality
e  § Containerized application using Docker and deployed to AWS, ensuring secure, scalable access for users with minimal latency
Al Flashcards | OpenAl, Stripe, React, Next.js, Firebase, Material UI, CSS

e@ = Created a full stack application that can generate flashcards for any subject using OpenAl, along with enabling real-time data
synchronization and cloud storage of all flashcards for each user using Firebase

e@ Implemented user authentication and management using Clerk API, integrating secure multi-factor authentication, OAuth sign-ins
and user session handling
e Configured Stripe API to handle secure payment processing, including credit card transactions, subscription management, and
invoicing
ACTIVITIES AND EXTRACURRICULARS
Google’s Sponsored Quantum UP! Challenge Hartford, Connecticut
e Tied for 1° in the Quantum Up Quantum Computing Challenge specializing in Quantum Power

e Participated in a series of educational seminars related to the ethics, applications, and impacts of quantum technologies
e Developed a real life solution and provided strategic recommendations for utilizing quantum technologies efficiently in the future

Cyber Security Club Storrs, Connecticut
e Learn about different Cybersecurity concepts and participate in the National Cyber League CTF Competitions
e Team placed 199/4672 in the fall CTF competition, scoring in the 96th percentile of competitors


    """
    
    resume_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "phone": {"type": "string"},
            "location": {"type": "string"},
            "experience": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "position": {"type": "string"},
                        "company": {"type": "string"},
                        "duration": {"type": "string"}
                    }
                }
            },
            "education": {"type": "string"},
            "skills": {
                "type": "array", 
                "items": {"type": "string"}
            }
        },
        "required": ["name", "experience", "skills"]
    }
    
    print("\n=== RESUME EXTRACTION ===")
    resume_result = extract_document_to_json(resume_text, resume_schema)
    resume_json = json.loads(resume_result['choices'][0]['message']['content'])
    
    # Print to console
    print("Generated JSON:")
    print(json.dumps(resume_json, indent=2))
    
    # Write to file
    write_to_file("resume_outputEthan.txt", json.dumps(resume_json, indent=2))

if __name__ == "__main__":
    main()