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

    # -----------------------------
    # INSERT METHODS
    # -----------------------------

    def save_to_database(self):
        sql = "INSERT INTO students (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (self.student_number, self.name, self.surname, self.birthdate, self.gender)
        try:
            Student.cursor.execute(sql, values)
            Student.connection.commit()
            print(f"{self.name} {self.surname} added to database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    @staticmethod
    def save_all_students(students):
        sql = "INSERT INTO students (student_number, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        try:
            Student.cursor.executemany(sql, students)
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} students added to database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # -----------------------------
    # SELECT METHODS
    # -----------------------------

    @staticmethod
    def student_info():
        # sql = "SELECT * FROM students"
        # sql = "SELECT student_number, name, surname FROM students WHERE gender = 'F'"
        # sql = "SELECT student_number, name, surname FROM students WHERE YEAR(birthdate) = 2003"
        # sql = "SELECT student_number, name, surname FROM students WHERE name LIKE '%an%'"
        sql = "SELECT COUNT(student_id) FROM students WHERE gender = 'M'"  

        try:
            Student.cursor.execute(sql)
            result = Student.cursor.fetchone()
            print(f"Result: {result[0]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # -----------------------------
    # UPDATE METHODS
    # -----------------------------

    @staticmethod
    def update_student(id, name, surname):
        sql = "UPDATE students SET name = %s, surname = %s WHERE student_id = %s"
        values = (name, surname, id)
        try:
            Student.cursor.execute(sql, values)
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} record updated.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    @staticmethod
    def update_student_by_gender(gender):
        sql = "UPDATE students SET name = CONCAT('Mr ', name) WHERE gender = %s"
        values = (gender,)
        try:
            Student.cursor.execute(sql, values)
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} record updated.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # -----------------------------
    # CLEANUP METHODS
    # -----------------------------

    @staticmethod
    def close_connection():
        try:
            Student.cursor.close()
            Student.connection.close()
            print("Database connection closed.")
        except:
            pass


# -----------------------------
# USİNG EXAMPLES
# -----------------------------

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

Student.save_all_students(students)

# Student.update_student(2, "Ahmet", "Can")

# Student.update_student_by_gender("M")

# Student.student_info()

Student.close_connection()
