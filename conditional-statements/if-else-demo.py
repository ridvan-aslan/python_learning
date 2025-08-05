from datetime import datetime
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# education = int(input("Enter your education level (1 - Middle school, 2 - High school, 3 - University): "))

# if age >= 18 and education != 1 :
#     print("You can get a driver's license.")
# else:
#     print("You cannot get a driver's license.")

# new section

# written_exam1 = int(input("Enter your first written exam result: "))
# written_exam2 = int(input("Enter your second written exam result: "))
# oral_exam = int(input("Enter your oral exam result: "))

# average = (written_exam1 + written_exam2 + oral_exam) / 3

# if average <= 24:
#     grade = 0
# elif average <= 44:
#     grade = 1
# elif average <= 54:
#     grade = 2
# elif average <= 69:
#     grade = 3
# elif average <= 84:
#     grade = 4
# else:
#     grade = 5

# print(f"Average: {average:.2f}, Grade: {grade}")

#new section

date_str = input("Since when have you been using your vehicle?  (YYYY-MM-DD): ")
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

date_difference = (datetime.now() - date_obj).days
maintenance_level = date_difference // 365

if maintenance_level != 0 :
   print(f"Service interval: {maintenance_level}")
else:
   print("No service required yet.")




