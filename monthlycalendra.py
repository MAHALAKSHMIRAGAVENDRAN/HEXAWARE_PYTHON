import math
from datetime import datetime

expenses = {}

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent): ")
    amount = float(input("Enter amount: "))
    expenses.setdefault(date, []).append((category, amount))
    print("Expense added successfully.\n")

def show_monthly_summary():
    monthly_summary = {}
    for date, items in expenses.items():
        month = date[:7]  # YYYY-MM
        monthly_summary.setdefault(month, 0)
        for cat, amt in items:
            monthly_summary[month] += amt
    for month, total in monthly_summary.items():
        print(f"Total for {month}: ₹{math.ceil(total)}")

# Demo
add_expense()
add_expense()
show_monthly_summary()
