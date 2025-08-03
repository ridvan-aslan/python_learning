from datetime import datetime

cars = ["Bmw" , "Mercedes", "Toyota", "Honda", "Ford"]

# print(len(cars))  
# print(cars[0])
# print(cars[-1])

cars[-1] = "Audi"

# print(cars.count("Bmw"))
# print(cars.index("Toyota"))

result = "Mercedes" in cars
print(result)

# print(cars[-2])
# print(cars[:3])

cars[-2:] = ["Volkswagen", "Hyundai"]
cars.append("Nissan")
cars.insert(2, "Kia")

new_cars = cars + ["Peugeot", "Fiat"]
# print(new_cars)

cars.pop()  
cars.reverse()
# cars = cars[::-1] 

print(cars)

studentA = ["Rıdvan", "Aslan", 2003, [100, 100, 100]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ali", "Yılmaz", 2000, [90, 85, 95]]

print(f"{studentA[0]} {studentA[1]}, {datetime.now().year - studentA[2]} yaşında ve not ortalaması: {sum(studentA[3]) / len(studentA[3])}")