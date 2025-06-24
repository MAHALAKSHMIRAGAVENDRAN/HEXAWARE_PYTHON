
import json

print("1. Reading JSON from 'data.json':")
try:
    with open('data.json', 'r') as file:
        data_from_file = json.load(file)
    print(data_from_file)
except FileNotFoundError:
    print("data.json not found. Skipping file reading.")
except json.JSONDecodeError:
    print("data.json contains invalid JSON.")

print("\n2. Parsing JSON string:")
try:
    json_string = '{"name": "John", "age": 38, "city": "New York"}'
    parsed_data = json.loads(json_string)
    print(parsed_data)
except json.JSONDecodeError:
    print("Invalid JSON string.")

print("\n3. Writing dictionary to 'output.json':")
data_to_save = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "SQL", "Machine Learning"]
}
try:
    with open('output.json', 'w') as file:
        json.dump(data_to_save, file, indent=4)
    print("Data written to output.json successfully.")
except IOError:
    print("Error writing to output.json.")

print("\n4. Converting dictionary to JSON string:")
try:
    json_data = json.dumps(data_to_save, indent=4)
    print(json_data)
except (TypeError, ValueError):
    print("Failed to convert dictionary to JSON string.")
