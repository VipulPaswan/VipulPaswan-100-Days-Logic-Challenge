# Day 23 – Reading XML Data Using Python

This folder contains a Python script that reads and parses `employee.xml` using the `xml.etree.ElementTree` module.  
This continues from **Day 22**, where I created an XML document along with its XSD schema.  
Today’s focus was on how backend systems extract and use XML data in real applications.

---

## 📘 What This Project Does

Using Python, I:

- Loaded an XML file (`employee.xml`)
- Parsed each `<employee>` entry
- Extracted:
  - name  
  - age  
  - gender  
  - email  
  - phone  
  - address  
- Printed the data in a clean, formatted table
- Understood how XML transforms into backend-friendly data

---

## 🧠 Concepts Learned

### ✔ XML Parsing with Python
Using:

```python
import xml.etree.ElementTree as ET

✔ Extracting Data

.find() for child elements

.text to get data content

.findall('employee') to loop through multiple entries

✔ Formatting Output

Used formatted printing:

print("{:<12} | {:<5} | {:<8}".format())


This converts hierarchical XML data into a tabular structure, just like real backend systems.

🔗 Connection: Day 22 → Day 23
Day	Topic	What Happened
Day 22	XML + XSD	Data defined + validated
Day 23	Read XML using Python	Data extracted + processed

This flow represents how real enterprise pipelines work:

XML → XSD Validation → Parsing → Database / Output

📦 Files Included
Day_23/
│── employee.xml            # XML input file
│── employee.xsd            # Schema (from Day 22)
│── read_xml.py             # Python parser script
│── README.md               # Documentation

🔧 Technologies Used

Python

xml.etree.ElementTree

XML / XSD

Formatted console output

🎯 Why This Matters

Parsing XML is essential in:

ERP systems

Government data exchange

Banking APIs

Billing systems

Android development

SOAP-based services

Invoice & report generation

Understanding this workflow builds strong backend fundamentals.

🚀 Next Steps

Convert XML → JSON

Store XML data in database

Build mini GUI to display employee list

Validate XML inside Python using XSD