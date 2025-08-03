x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# result = (number1 * number2) - (x + y + z)

# y //= x 

result = (x + y + z) % 3

print(f"The result of the calculation is: {result}")

# y **= x 

# print(f"The value of y after exponentiation is: {y}")

x, *y, z = numbers

print(f"x: {x}, y: {y}, z: {z}")

z **= 3

print(f"The value of z after exponentiation is: {z}")

total = 0

for x in y :
  total += x 

print(total)


