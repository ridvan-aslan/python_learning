from datetime import datetime  

website = "https://www.google.com/"
course = "Python Programming"

length = len(course)

# print(f"Course: {course}, Length: {length}")
# print(f"www : {website[8:11]}")
# print(f"com : {website[-4:-1]}")
# print(f"first 15 characters in course : {course[:15]}")
# print(f"last 15 characters in course : {course[-15:]}")
# print(f"Course characters reversed: {course[::-1]}")

name, surname, age, job = "Rıdvan", "Aslan", datetime.now().year - 2003, "Software Developer"

print(f"My name is {name} {surname}, I am {age} years old and I work as a {job}.")

word = "Hello world"
word = word[0:6] + "W" + word[7:]   

# word = word.replace("w", "W")

print(f"Modified word: {word}")
print(f"Repeated word: {'abc' * 3}")