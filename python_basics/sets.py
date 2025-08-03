fruits = {"apple", "banana", "cherry"}

# print(fruits[0]) # This will raise an error because sets do not support indexing

for fruit in fruits:
    print(fruit)

fruits.add("orange") 
fruits.update(("kiwi", "melon", "apple"))

fruits.remove("banana")
fruits.discard("apple")  
fruits.pop()  
# fruits.clear()

print(fruits)

my_list = [1, 2, 3, 4, 5, 5, 2, 2, 1]
my_set = set(my_list)  

print(my_set)  