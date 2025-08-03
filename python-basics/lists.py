from datetime import datetime

message = "Hello There. My name is Rıdvan Aslan.".split(" ")

# print(message[0])

my_list = [1, 2, 3]
my_list = [1 , "two", True, 4.5]

# print(my_list)

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]
numbers = list1 + list2

print(numbers)
print(len(numbers))
print(message[0])
print(message[3])

userA = ["Rıdvan", datetime.now().year - 2003]
userB = ["Ali", datetime.now().year - 2000]
users = [userA, userB]

print(users)
print(userA)
print(userB)

print(users[0][0])
print(users[0][1])