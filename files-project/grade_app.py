def calculate_grade(line):
    line = line.strip()
    my_list = line.split(":")
    grade_list = my_list[1].strip().split(",")

    total = 0
    for i in range(len(grade_list)):
        total += float(grade_list[i])
        
    average = total / len(grade_list)

    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    return f"{my_list[0]}: {average:.2f} ({letter_grade})"

def read_average():
    with open('files-project/grades.txt', 'r', encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))

def write_grades():
    name = input("Enter the student's name: ")
    surname = input("Enter the student's surname: ")
    grades = []
    for i in range(3):
        grade = input(f"Enter grade {i+1}: ")
        try:
            grades.append(float(grade))
        except ValueError:
            print("Invalid input. Please enter a number.")

    with open('files-project/grades.txt', 'a', encoding="utf-8") as file:
        file.write(f"{name} {surname}: {grades[0]}, {grades[1]}, {grades[2]}\n")
        print(f"Grades for {name} {surname} saved successfully.")
def save_grades():
    with open('files-project/grades.txt', 'r', encoding="utf-8") as file1:
        my_list = []

        for i in file1:
            my_list.append(i)

    with open('files-project/results.txt', 'w', encoding="utf-8") as file2:
        for i in my_list:
            file2.write(i)

            



while True:
    operation = input(
    "1-Read Grades\n"
    "2-Write Grades\n"
    "3-Save Grades\n"
    "4-Exit or write 'exit'\n"
    "Select an operation: "
)
    if operation == "1":
        read_average()
    elif operation == "2":
        write_grades()
    elif operation == "3":
        save_grades()
    elif operation == "4" or operation.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid operation. Please try again.")
