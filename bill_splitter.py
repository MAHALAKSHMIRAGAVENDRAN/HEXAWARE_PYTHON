import math

def bill_splitter():
    names = input("Enter names separated by comma: ").split(",")
    total = float(input("Enter total bill amount: ₹"))
    per_person = list(map(lambda _: round(total / len(names), 2), names))
    result = dict(zip(names, per_person))
    for person, amt in result.items():
        print(f"{person.strip()} pays ₹{amt}")

# Demo
bill_splitter()
