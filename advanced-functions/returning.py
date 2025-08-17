# def power(number):
#     def inner(power):
#         return number ** power
#     return inner

# two = power(2)
# three = power(3)

# print(two(3))
# print(three(2))

# def query_authority(page):
#     def inner(role):
#         if role == "admin":
#             return f"Access granted to {page} for {role}"
#         else:
#             return f"Access denied to {page} for {role}"
#     return inner

# home_page = query_authority("home")

# print(home_page("user"))
# print(home_page("admin"))

def operation(operation_name):
    def add(*args):
        result = 0
        for i in args:
            result += i
        return result
    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result
    
    if operation_name == "add":
        return add
    else:
        return multiply

add_function = operation("add")
multiply_function = operation("multiply")

print(add_function(1, 2, 3, 4, 5))
print(multiply_function(1, 2, 3, 4, 5))
        
    


