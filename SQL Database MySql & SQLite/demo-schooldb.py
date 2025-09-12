import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    cursor = connection.cursor()

    def __init__(self, student_number, name, surname, birthdate, gender):
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def save_to_database(self):
        sql = "INSERT INTO students (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (self.student_number, self.name, self.surname, self.birthdate, self.gender)
        try:
            Student.cursor.execute(sql, values)
            Student.connection.commit()
            print(f"{self.name} {self.surname} added to database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            print("Operation finished.")
            Student.cursor.close()
            Student.connection.close()
            print("Database connection closed.")

    @staticmethod
    def save_all_students(students):
        sql = "INSERT INTO students (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (students)
        try:
            Student.cursor.executemany(sql, values)
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} students added to database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            print("Operation finished.")
            Student.cursor.close()
            Student.connection.close()
            print("Database connection closed.")

    @staticmethod
    def student_info():
        # sql = "SELECT * FROM students"
        # sql = "SELECT student_number, name, surname FROM students"
        # sql = "SELECT student_number, name, surname FROM students where gender = 'F'"
        # sql = "SELECT student_number, name, surname FROM students where YEAR(birthdate) = 2003"
        # sql = "SELECT student_number, name, surname FROM students where name = 'Ayşe' and YEAR(birthdate) = 2004"
        # sql = "SELECT student_number, name, surname FROM students where name LIKE '%an%'"
        sql = "SELECT COUNT(student_id) FROM students where GENDER = 'm'"
        # sql = "SELECT student_number, name, surname FROM students WHERE gender = 'F' ORDER BY name"

        try:
            Student.cursor.execute(sql)

            # result = Student.cursor.fetchone()
            # print(f"Number of male students: {result[0]}")

            result = Student.cursor.fetchall()
            for row in result:
                print(f"Student Number: {row[0]}, Name: {row[1]}, Surname: {row[2]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            Student.cursor.close()
            Student.connection.close()

            
Student.student_info()

# student = Student("109", "Ayşe", "Demir", datetime(2002, 3, 15), "F")
# student.save_to_database()

students = [
    ("201", "Ahmet", "Can", datetime(2003, 5, 10), "M"),
    ("202", "Büşra", "Demir", datetime(2004, 2, 20), "F"),
    ("203", "Cem", "Yılmaz", datetime(2002, 10, 1), "M"),
    ("204", "Deniz", "Kara", datetime(2005, 4, 15), "F"),
    ("205", "Emre", "Gümüş", datetime(2003, 8, 12), "M"),
    ("206", "Fatma", "Tekin", datetime(2004, 7, 5), "F")
]

# Student.save_all_students(students)

# cursor = connection.cursor()

# students = [
#     ("101", "Rıdvan", "Aslan", datetime(2003, 7, 5), "M"),
#     ("102", "Ayşe", "Yılmaz", datetime(2004, 1, 15), "F"),
#     ("103", "Mehmet", "Demir", datetime(2002, 11, 20), "M"),
#     ("104", "Zeynep", "Can", datetime(2005, 3, 10), "F"),
#     ("105", "Ali", "Kara", datetime(2003, 9, 25), "M"),
#     ("106", "Elif", "Tekin", datetime(2004, 6, 30), "F")
# ]

# def insert_students(students):
#     sql = "INSERT INTO students (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
#     value = (students)

#     try:
#         cursor.executemany(sql, value)
#         connection.commit()
#         print(cursor.rowcount, "record inserted.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#     finally:
#         cursor.close()
#         connection.close()
#         print("Database connection closed.")

# insert_students(students)
# print("Data sent to the database.")