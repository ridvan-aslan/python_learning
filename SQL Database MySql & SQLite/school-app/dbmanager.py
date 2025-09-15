from connection import connection
from datetime import datetime
from student import Student
from teacher import Teacher


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM student WHERE id = %s"
        self.cursor.execute(query, (student_id,))

        try:
            student_data = self.cursor.fetchone()
            if student_data:
                return Student.create_student(student_data)
            else:
                return None
        except Exception as e:
            print(f"Error fetching student by ID: {e}")

    def get_students_by_class_id(self, class_id):
        query = "SELECT * FROM student WHERE class_id = %s"
        self.cursor.execute(query, (class_id,))
        try:
            student_data = self.cursor.fetchall()
            if student_data:
                return Student.create_student(student_data)
            else:
                return []
        except Exception as e:
            print(f"Error fetching students by class ID: {e}")
    
    def add_student(self, student: Student):
        sql = "INSERT INTO student (student_number, name, surname, birthdate, gender, class_id) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (student.student_number, student.name, student.surname, student.birthdate, student.gender, student.class_id)
        try:
            self.cursor.execute(sql, value)  
            self.connection.commit()
            print(f"{self.cursor.rowcount} student added to database.")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
        

    def edit_student(self, student: Student):
        sql = "UPDATE student SET name = %s, surname = %s, birthdate = %s, gender = %s, class_id = %s WHERE student_number = %s"
        values = (student.name, student.surname, student.birthdate, student.gender, student.class_id, student.student_number)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            print(f"{self.cursor.rowcount} record updated.")
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def delete_student(self, student_id):
        query = "DELETE FROM student WHERE id = %s"
        try:
            self.cursor.execute(query, (student_id,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                print(f"{self.cursor.rowcount} student deleted.")
            else:
                print("No student found with the given ID.")
        except Exception as e:
            print(f"Error deleting student: {e}")
            self.connection.rollback()


    def add_teacher(self, teacher: Teacher):
        pass

    def edit_teacher(self, teacher: Teacher):
        pass

    def close(self):
        self.connection.close()
        print("Database connection closed.")



