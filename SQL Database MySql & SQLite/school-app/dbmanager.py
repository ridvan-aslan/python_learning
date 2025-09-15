from connection import connection
from datetime import datetime
from student import Student
from teacher import Teacher


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def add_student(self, student: Student):
        pass

    def edit_student(self, student: Student):
        pass

    def add_teacher(self, teacher: Teacher):
        pass

    def edit_teacher(self, teacher: Teacher):
        pass

