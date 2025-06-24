import mysql.connector

try:
    db = mysql.connector.connect(host="localhost", user="root", passwd="", database="hexaware")
    c = db.cursor()
    c.execute("SELECT * FROM employee")
    for r in c.fetchall():
        print(r)
except mysql.connector.Error as e:
    print("Database error:", e)
finally:
    if 'c' in locals():
        c.close()
    if 'db' in locals() and db.is_connected():
        db.close()
