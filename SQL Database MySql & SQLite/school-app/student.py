class Student:
    def __init__(self, student_number, name, surname, birthdate, gender, class_id):
        self.id = id
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.class_id = class_id

    @staticmethod
    def create_student(student_data):
        my_list = []

        if isinstance(student_data, tuple):
            my_list.append(Student(*student_data[1:]))
        else:
            for i in student_data:
                my_list.append(Student(*i[1:]))

        return my_list

    