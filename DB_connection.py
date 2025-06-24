import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS HEXAWARE")
cursor.execute("USE HEXAWARE")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    number VARCHAR(15),
    depart VARCHAR(50),
    gender VARCHAR(10),
    salary DECIMAL(10, 2)
)
""")
print("table created successfully.")

cursor.close()
db.close()
