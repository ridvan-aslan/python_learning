from datetime import datetime
def say_hello(name = "User"):
    return "Hello " + name
 
msg = say_hello("Rıdvan")

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(2, 3)

print(result)

def calculate_age(birth_year):
    return datetime.now().year - birth_year

age_ridvan = calculate_age(2003)
age_ada = calculate_age(2005)
age_sena = calculate_age(2000)

print(age_ridvan)
print(age_ada)
print(age_sena)

# print(help(list.append))