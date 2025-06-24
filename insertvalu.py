import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hexaware")
c = db.cursor()

query = "INSERT INTO employee (id, name, number, depart, gender, salary) VALUES (%s, %s, %s, %s, %s, %s)"
data = [
    (1, "Ram", "9876543210", "HR", "Male", 50000),
    (2, "Priya", "8765432109", "IT", "Female", 60000),
    (3, "Kumar", "7654321098", "Admin", "Male", 40000)
]

c.executemany(query, data)
db.commit()
print("Employee records inserted successfully.")

c.close()
db.close()
