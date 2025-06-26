import math
from datetime import date

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter 3 subject marks separated by space: ").split()))
    total = sum(marks)
    avg = total / len(marks)
    grade = (lambda avg: 'A' if avg >= 90 else 'B' if avg >= 75 else 'C' if avg >= 50 else 'F')(avg)
    students[name] = {'marks': tuple(marks), 'total': total, 'avg': round(avg, 2), 'grade': grade}

def show_report():
    for name, info in students.items():
        print(f"{name} - Marks: {info['marks']}, Total: {info['total']}, Avg: {info['avg']}, Grade: {info['grade']}")

# Demo
add_student()
show_report()
