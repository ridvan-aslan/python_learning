from datetime import datetime # Importing datetime module to work with dates and times

name = "Rıdvan"
surname = "Aslan"
birth_year = 2003
age = datetime.now().year - birth_year

# print("My name is {} {}".format(name, surname))
# print("My name is {1} {0}".format(name, surname))
# print("My name is {s} {n}".format(n = name, s = surname))
# print("My name is {n} {s} and I am {a} years old.".format(n = name, s = surname, a = age))

result = 200/700
# print("The result is {:.2f}".format(result))  

print(f"My name is {name} {surname} and I am {age} years old.")