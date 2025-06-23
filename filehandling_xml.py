from bs4 import BeautifulSoup

# Sample XML
xml_data = """<?xml version="1.0"?>
<students>
    <student name="Maha" age="21"/>
    <student name="Janani" age="25"/>
</students>
"""

# Write XML to file
with open("sample.xml", "w") as f:
    f.write(xml_data)

# Read XML
with open("sample.xml", "r") as f:
    data = f.read()
soup = BeautifulSoup(data, "xml")
students = soup.find_all("student")
for s in students:
    print(s["name"], s["age"])
