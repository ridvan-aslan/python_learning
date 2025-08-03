my_list = [1, 2, 3]
my_tuple = (1, "iki", 3.0)

print(type(my_list), type(my_tuple))
print(my_list[0])
print(my_tuple[1])
print(len(my_list), len(my_tuple))

my_list = ["Ali", "Ayşe", "Mehmet"]
my_tuple = ("Veli", "Fatma", "Ahmet")
names = ("Rıdvan", "Elif", "Burak", "Deniz", "Seda") + my_tuple

print(names)

my_list[0] = "Rıdvan"
# my_tuple[1] = "Zeynep"  # Tuples are immutable, this will raise an error

print(my_list)
print(my_tuple)

print(my_list.count("Rıdvan"))
print(my_tuple.count("Veli"))

print(my_list.index("Ayşe"))
print(my_tuple.index("Fatma"))
