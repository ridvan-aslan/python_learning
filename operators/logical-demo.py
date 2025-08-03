# number = int(input("Enter a number: "))

# if number > 0 and number < 100:
#     print(f"{number} is between 0 and 100")
# else:
#     print(f"{number} is not between 0 and 100")


# if number > 0 and number % 2 == 0:
#     print(f"{number} is positive and even")

#new section

# username = "ridvanaslan"
# password = "12345"

# if username == "ridvanaslan" and password == "12345":
#     print("Access successful")

# new section

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))

# biggest = max(number1, number2, number3)
# print(f"{biggest} is the biggest number")


# new section

# visa1 = float(input("Enter your first midterm exam result: "))
# visa2 = float(input("Enter your second midterm exam result: "))
# final = float(input("Enter your final exam result: "))

# average = (((visa1 + visa2 ) / 2  ) * 0.6) + (final * 0.4)

# print(f"Your overall average is: {average}")

# if (average >= 50 and final >=50) or (final >=70):
#     print("You passed!")
# else: 
#     print("You failed.")

# new section

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height_m = float(input("Enter your height (cm): ")) / 100

bmi = weight / height_m ** 2

if bmi <= 0:
    category = "Invalid value"
elif bmi < 18.5:
    category = "underweight"
elif bmi <= 24.9:
    category = "normal weight"
elif bmi <= 29.9:
    category = "overweight"
elif bmi <= 34.9:
    category = "obese"
else:
    category = "out of the specified range"

print(f"{name}, your BMI is {bmi:.2f}. You are {category}.")
