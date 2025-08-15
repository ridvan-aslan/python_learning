# error handling

# try:
#     number1 = int(input("Enter a number: "))
#     number2 = int(input("Enter another number: "))
#     result = number1 / number2
#     print(f"The result is: {result}")
# except (ZeroDivisionError, ValueError) as e:
#     print(f"An error occurred: {e}")

# try:
#     number1 = int(input("Enter a number: "))
#     number2 = int(input("Enter another number: "))
#     result = number1 / number2
#     print(f"The result is: {result}")
# except:
#     print("An error occurred. Please try again.")
  
while True:
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        result = number1 / number2
        print(f"The result is: {result}")
    except Exception as e:
        print("An error occurred. Please try again. ", e)
    else:
        break
    finally:
        print("This block always executes, regardless of an error.")