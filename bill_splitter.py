import math

def bill_splitter():
    n = int(input("Enter number of people: "))
    names = [input(f"Enter name {i+1}: ") for i in range(n)]
    total = float(input("Enter total bill amount: ₹"))
    per_person = list(map(lambda _: round(total / n, 2), names))
    result = dict(zip(names, per_person))
    for person, amt in result.items():
        print(f"{person.strip()} pays ₹{amt}")

# Demo
bill_splitter()
