import sqlite3

connection = sqlite3.connect("SQL Database MySql & SQLite/chinook.db")

cursor = connection.cursor()

cursor.execute("Select * from customers")
result = cursor.fetchall()

for i in result:
    print(i)

connection.close()