numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# for x in numbers :
#     if x % 3 == 0:
#         print(x)

# new section 

# total = 0

# for x in numbers:
#     total += x

# print(f"The total of numbers: {total}")

# new section 

# odd_squares = [x ** 2 for x in numbers if x % 2 == 1]

# print("The square of odd numbers are:", odd_squares)

# new section

# cities = ["Kocaeli", "İstanbul", "Tekirdağ", "İzmir","Rize"]

# for city in cities:
#     if len(city) <= 5:
#         print(city)

# new section

products = [
    {'name' : 'Samsung s6', 'price' : '3000'},
    {'name' : 'Samsung s7', 'price' : '4000'},
    {'name' : 'Samsung s8', 'price' : '5000'},
    {'name' : 'Samsung s9', 'price' : '6000'},
    {'name' : 'Samsung s10', 'price' : '7000'},
]

# total = 0

# for product in products: 
#     total += int(product['price'])

# print("The total price of the products is:", total)

# new question about products

for product in products:
    if int(product['price']) > 5000:
        print(product['name'])



    
