names = ["Rıdvan", "Ali", "Ayşe", "Fatma", "Mehmet"]
years = [2003, 1985, 2000, 1995, 1988]

names.append("Zeynep")
names.insert(1, "Emre")

# names.remove("Fatma")
# names.pop(2)

# print(names.index("Fatma")) 
# print(names.count("Ali"))
# result = "Ali" in names
# print(result)

names.reverse()
names.sort()
years.sort()
years.reverse()

print(min(years), max(years))
print(years.count(2000))

years.clear()

print(names) 
print(years)

s = "Chevrolet, Ford, Toyota, Honda, BMW"
print(s.split(", "))

cars = []

car1 = input("Enter the first car brand: ")
car2 = input("Enter the second car brand: ")
car3 = input("Enter the third car brand: ")

cars.append(car1)
cars.append(car2)
cars.append(car3)

print(cars)