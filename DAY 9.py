
# 1. First Python Program
print("Welcome to Python World!")

# 2. Variables & Data Types
x = 10
y = 3.5
name = "Maha"
z = True
print(x, y, name, z)

# 3. Operators
a = 15
b = 4
print("Add:", a + b)
print("Divide:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 4. Data Types
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("List:", fruits)

colors = ("red", "green", "blue")
print("Tuple:", colors)

unique_nums = {1, 2, 2, 3}
print("Set:", unique_nums)

student = {"name": "Maha", "age": 21}
print("Dictionary:", student)

# 5. If-Else & Elif
n = 10
if n > 10:
    print("Greater than 10")
elif n == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# 6. For Loop & While Loop
for i in range(3):
    print("For Loop:", i)

i = 0
while i < 3:
    print("While Loop:", i)
    i += 1

# 7. Break, Continue, Pass
for i in range(5):
    if i == 3:
        break
    print("Break:", i)

for i in range(5):
    if i == 3:
        continue
    print("Continue:", i)

for i in range(2):
    pass
print("Pass executed")

# 8. Input & Output (commented to avoid errors during execution)
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("Sum:", x + y)

# 9. String Functions
s = " Hello Python "
print(s.strip())
print(s.upper())
print(s.lower())
print(s.replace("Python", "World"))
print("Length:", len(s))

# 10. Number Functions
import math
print("Square root of 25:", math.sqrt(25))
print("Power 2^3:", math.pow(2, 3))
print("Pi value:", math.pi)

# 11. Date and Time
import time
import calendar
print("Current Time:", time.asctime())
print(calendar.month(2025, 6))

# 12. Simple Function
def greet(name):
    print("Hello", name)
greet("Maha")

# 13. Function with Arguments
def employeeDetails(eid, ename):
    print("ID:", eid)
    print("Name:", ename)
employeeDetails(31410, "Vimala")

# 14. *args and **kwargs
def show_args(*args):
    print("Args:", args)
def show_kwargs(**kwargs):
    print("Kwargs:", kwargs)
show_args(1, 2, 3)
show_kwargs(name="Maha", age=21)

# 15. Class and Object
class Computer:
    def config(self):
        print("16GB RAM, 1TB SSD")
c = Computer()
c.config()

# 16. Constructor
class Student:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Student Name:", self.name)
s = Student("Maha")
s.show()

# 17. Access Specifiers
class Employee:
    def __init__(self):
        self.name = "Public"
        self._dept = "Protected"
        self.__salary = 50000
    def show(self):
        print(self.name)
        print(self._dept)
        print(self.__salary)
e = Employee()
e.show()

# 18. Inheritance
class Project:
    def project1(self):
        print("Project 1")
class Admin(Project):
    def project2(self):
        print("Project 2")
a = Admin()
a.project1()
a.project2()

# 19. Polymorphism
print(len("Python"))
print(len([1, 2, 3]))
print("Maha" + " Lakshmi")
print(10 + 20)

# 20. Method Overriding
class Customer:
    def details(self):
        print("Customer Details")
class Order(Customer):
    def details(self):
        print("Order Details")
o = Order()
o.details()
