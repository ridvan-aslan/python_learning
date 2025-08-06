# numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# new section

# number1 = int(input("Enter your starting number: "))
# number2 = int(input("Enter your ending number: "))

# i = number1

# while i <= number2 :
#     if i % 2 == 1:
#         print(i)
#     i += 1

# new section

# i = 100

# while i >= 1 :
#     print(i)
#     i -= 1

# new section

# numbers = []
# i = 0

# while i < 5:
#     number = int(input(f"Enter number {i + 1}: "))
#     numbers.append(number)
#     i += 1

# numbers.sort()
# print(f"The numbers you entered in ascending order are: {numbers}")

# new section

products = []

piece = int(input("How many products do you want to add: "))
i = 0

while i < piece :
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")

    products.append({
        "name": product_name,
        "price":  product_price
    })
    i += 1

for product in products:
    print(f"Product name: {product["name"]}, Product price: {product["price"]}")
