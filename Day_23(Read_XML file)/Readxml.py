import xml.etree.ElementTree as ET

tree = ET.parse('employee.xml')
root = tree.getroot()


print("{:<12} | {:<5} | {:<8} | {:<25} | {:<12} | {:<10}".format(
    "Name", "Age", "Gender", "Email", "Phone", "Address"
))
print("-" * 90)

for emp in root.findall('employee'):
    name = emp.find('name').text
    age = emp.find('age').text
    gender = emp.find('gender').text
    email = emp.find('email').text
    phone = emp.find('phone').text
    address = emp.find('address').text

    print("{:<12} | {:<5} | {:<8} | {:<25} | {:<12} | {:<10}".format(
        name, age, gender, email, phone, address
    ))



