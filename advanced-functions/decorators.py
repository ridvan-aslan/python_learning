import time
import math

# def my_decorator(func):
#     def wrapper(name):
#         print("Something is happening before the function is called.")
#         func(name)
#         print("Something is happening after the function is called.")

#     return wrapper


# @my_decorator
# def say_hello(name):
#     print("Hello!", name)

# say_hello("Rıdvan")  

def calculate_time(func): 
    def inner(*args, **kwargs): 
        start_time = time.time() 
        time.sleep(1)
        print(func(*args, **kwargs))
        finish = time.time()
        print(f"Function {func.__name__} ran in {finish - start_time} seconds")
    return inner
     

@calculate_time 
def power(a, b):
    return math.pow(a, b)

@calculate_time 
def factorial(number):
    return math.factorial(number)

@calculate_time
def add(*args):
    result = 0
    for i in args:
        result += i
    return result

power(2, 3)
factorial(5)
add(1, 2, 3, 4, 5)

