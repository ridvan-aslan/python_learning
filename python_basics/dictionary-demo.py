students = {
    "120": {
        "name": "Alice",
        "surname": "Smith",
        "age": 20,
    },
    "121": {
        "name": "Bob",
        "surname": "Johnson",
        "age": 22,
    },
    "122": {
        "name": "Carol",
        "surname": "Williams",
        "age": 19,
    }
}

student_id = input("Enter student ID: ")

if student_id in students:
    print(f"Error: Student with ID {student_id} already exists. Please choose a different ID or update the existing record.")
else:
    student_name = input("Enter student name: ")
    student_surname = input("Enter student surname: ")
    student_age = int(input("Enter student age: "))
    # students[student_id] = {
    # "name": student_name,
    # "surname": student_surname,
    # "age": student_age
    # }   
    students.update({ 
        student_id: {
            "name": student_name,
            "surname": student_surname,
            "age": student_age
        }
    })

print(students)

show_students = input("Enter your student ID to view details: ")
if show_students in students:
    student = students[show_students]
    print(f"Name: {student['name']}, Surname: {student['surname']}, Age: {student['age']}")
else:
    print("Error: Student not found. Please check the ID and try again.")

     