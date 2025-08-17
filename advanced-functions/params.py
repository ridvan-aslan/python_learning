def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def operation(f1, f2, f3, f4, operation_name):
    if operation_name == "add":
        return f1
    elif operation_name == "subtract":
        return f2
    elif operation_name == "multiply":
        return f3
    elif operation_name == "divide":
        return f4
    else:
        raise ValueError("Invalid operation name")
    
add_function = operation(add, subtract, multiply, divide, "add")
subtract_function = operation(add, subtract, multiply, divide, "subtract")
multiply_function = operation(add, subtract, multiply, divide, "multiply")
divide_function = operation(add, subtract, multiply, divide, "divide")

print(add_function(5, 3))
print(subtract_function(5, 3))
print(multiply_function(5, 3))
print(divide_function(6, 3))

    