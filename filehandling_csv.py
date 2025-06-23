import csv

# Write to CSV
fields = ['Name', 'Age']
rows = [['Maha', 21], ['Janani', 25]]
with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)

# Read from CSV
with open("sample.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
