import pandas as pd

# 1. Excel File Handling
excel_data = pd.DataFrame({'Name': ['Maha', 'Janani'], 'Age': [21, 25]})
excel_data.to_excel("sample.xlsx", index=False)
read_excel = pd.read_excel("sample.xlsx")
print("Excel Data:")
print(read_excel)

# 2. CSV File Handling
csv_data = pd.DataFrame({'Name': ['Maha', 'Raj'], 'Marks': [85, 92]})
csv_data.to_csv("sample.csv", index=False)
read_csv = pd.read_csv("sample.csv")
print("\nCSV Data:")
print(read_csv)

# 3. JSON File Handling
json_data = pd.DataFrame({'EmpID': [101, 102], 'Salary': [50000, 60000]})
json_data.to_json("sample.json", orient="records", indent=4)
read_json = pd.read_json("sample.json")
print("\nJSON Data:")
print(read_json)

# 4. XML File Handling
xml_data = pd.DataFrame({'Student': ['Maha', 'Janani'], 'Score': [90, 95]})
xml_data.to_xml("sample.xml", index=False)
read_xml = pd.read_xml("sample.xml")
print("\nXML Data:")
print(read_xml)
