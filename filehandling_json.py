import json

# Write to JSON
data = {"students": [{"name": "Maha", "age": 21}, {"name": "Janani", "age": 25}]}
with open("sample.json", "w") as f:
    json.dump(data, f)

# Read from JSON
with open("sample.json", "r") as f:
    content = json.load(f)
    print(content)
