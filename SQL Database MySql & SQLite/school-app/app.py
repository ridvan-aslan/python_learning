from dbmanager import DbManager
from student import Student


class App:
    def __init__(self):
        self.db = DbManager()

    def init_app(self):
        message = "******\n1- Student List\n2- Add Student\n3- Edit Student\n4- Delete Student\n5- Exit\n******"
        while True:
            print(message)
            operation = input("Select operation: ") 

            if operation == "1":
                self.display_students()
            elif operation == "2":
                self.add_student()
            elif operation == "3":
                self.edit_student()
            elif operation == "4":
                self.delete_student()

            elif operation == "5":
                self.db.close()
                break
            else:
                print("Invalid operation selected.")

    def display_students(self):
        class_id = input("Enter class ID: ")
        students = self.db.get_students_by_class_id(class_id)
        for index, student in enumerate(students):
            print(f"{index+1}- {student.name} {student.surname}")

    def add_student(self):
        student_number = input("Enter student number: ")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        birthdate = input("Enter birthdate: ")
        gender = input("Enter gender: ")
        class_id = input("Enter class ID: ")   
        student = Student(student_number, name, surname, birthdate, gender, class_id)
        self.db.add_student(student) 

    def edit_student(self):
        student_id = input("Enter student ID to edit: ")
        student = self.db.get_student_by_id(student_id)

        student[0].name = input("Enter new name: ") or student[0].name
        student[0].surname = input("Enter new surname: ") or student[0].surname
        student[0].birthdate = input("Enter new birthdate: ") or student[0].birthdate
        student[0].gender = input("Enter new gender: ") or student[0].gender
        student[0].class_id = input("Enter new class ID: ") or student[0].class_id

        self.db.edit_student(student[0])

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        self.db.delete_student(student_id)

app = App()
app.init_app()