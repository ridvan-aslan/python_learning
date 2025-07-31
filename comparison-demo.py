# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 > number2:
#     print(f"Big number is: {number1}")
# elif number1 == number2:
#     print("Numbers are equal")
# else:
#     print(f"Big number is: {number2}")

# visa1 = float(input("Enter your first midterm exam result: "))
# visa2 = float(input("Enter your second midterm exam result: "))
# final = float(input("Enter your final exam result: "))

# average = (((visa1 + visa2 ) / 2  ) * 0.6) + (final * 0.4)

# print(f"Your overall average is: {average}")

# if average >= 50:
#     print("You passed!")
# else: 
#     print("You failed.")

# number = int(input("Enter a number: "))

# if number % 2 == 0 : 
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# if number > 0:
#     print(f"{number} is positive")
# elif number == 0 :
#     print(f"{number} is neither negative nor positive")
# else: 
#     print(f"{number} is negative")

username = "ridvanaslan"
password = "12345"

username_input = input("Enter your username: ")

if  username_input.strip().lower() == username: 
    password_input = input("Enter your password: ")   
    if password_input == password: 
        print("Access successful")
    else:
        print("Incorrect password.")
else:
    print("Invalid username. Please try again.")

