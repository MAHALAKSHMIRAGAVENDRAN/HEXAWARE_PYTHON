import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hexaware")
c = db.cursor()

print("All Employee Records:")
c.execute("SELECT * FROM employee")
for r in c.fetchall():
    print(r)

print("\nUpdating salary of employee with ID = 2")
c.execute("UPDATE employee SET salary = 65000 WHERE id = 2")
db.commit()
print("Salary updated.\n")

print("All Employee Records After Update:")
c.execute("SELECT * FROM employee")
for r in c.fetchall():
    print(r)

print("\nDeleting employee with ID = 3")
c.execute("DELETE FROM employee WHERE id = 3")
db.commit()
print("Employee deleted.\n")

print("All Employee Records After Deletion:")
c.execute("SELECT * FROM employee")
for r in c.fetchall():
    print(r)

c.close()
db.close()
