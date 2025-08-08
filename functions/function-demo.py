# def repeat_word(word, times):
#     for _ in range(times):
#         print(word)

# count = int(input("Enter the number of times the word will be repeated: "))
# repeat_word("Hello", count)

# new section

# def make_list(*args):
#     return list(args)

# items = make_list("item1", "item2", "item3")
# print("Items:", items)

# new section

# def print_primes(num1, num2):
#     while num1 < num2:
#         if num1 > 1:
#             for i in range(2, num1):
#                 if num1 % i == 0:
#                     break
#             else:
#                 print(f"{num1} is a prime number.")
#         num1 += 1

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# print_primes(number1, number2)

# new section

def print_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors .append(i)
    return divisors
    
number = int(input("Enter a number to find its divisors: "))
result = print_divisors(number)
print(f"The divisors of {number} are: {result}")




            
