# my_list = ["1", "2", "5a", "10b", "abc"]

# converted_list = []

# for item in my_list:
#     try:
#         converted_item = int(item)
#         converted_list.append(converted_item)
#     except ValueError:
#         pass

# print("Converted list:", converted_list)

# new section

# while True:
#     try:
#         user_input = int(input("Enter a number (or 'exit' to quit): "))
#         print(f"You entered: {user_input}")
#     except ValueError:
#         print("That's not a valid number. Please try again.")

# new section

# turkish_letters = "çğıöşüÇĞİÖŞÜ"

# def check_password(password):
#     if len(password) < 8:
#         raise ValueError("Password must be at least 8 characters long.")
#     if not any(char.isdigit() for char in password):
#         raise ValueError("Password must contain at least one digit.")
#     if not any(char.isalpha() for char in password):
#         raise ValueError("Password must contain at least one letter.")
#     if any(char in turkish_letters for char in password):
#         raise ValueError("Password cannot contain Turkish characters.")
    
# try:
#     check_password("Passw0rd")
# except ValueError as e:
#     print(f"Password validation failed: {e}")
# else:
#     print("Password is valid")

# new section
    
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n > 1000:
        raise OverflowError("Input is too large to compute factorial.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

numbers = [5, -3, 1001, "abc", 7]

for num in numbers:
    try:
        print(f"factorial({num}) =", factorial(num))
    except (ValueError, TypeError, OverflowError) as e:
        print(f"Factorial computation failed for input {num}: {e}")
