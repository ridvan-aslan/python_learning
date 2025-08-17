# def greeting(name):
#     print(f"Hello {name}")

# greeting("Rıdvan")
# print(greeting)

# say_hello = greeting

# del say_hello
# print(greeting)

#encapsulation

# def outer(number):
    
#     def inner_increment(number):
#         return number + 1
    
#     result = inner_increment(number)
#     print(number, result)

# outer(10)
# inner_increment(10) 

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    if not number >= 0:
        raise ValueError("Number must be zero or positive")

    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Example usage:
print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(-1)) # Raises ValueError
# print(factorial(2.5)) # Raises TypeError

