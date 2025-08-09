# class

class Person:
    pass # "pass" is a placeholder

    # class attributes    
    address = "Unknown"  

    # constructor
    def __init__(self, name, age):
        # object attributes
        self.name = name
        self.age = age
        print("Person created:", self.name, self.age)


    # methods

# object, instance

p1 = Person(name = "Alice", age =30) 
p2 = Person("Bob", 25)

# update object attributes
p1.address = "İstanbul"  
p2.address = "Tokyo"

# accessing attributes
print(f"p1: {p1.name}, {p1.age}, {p1.address}")
print(f"p2: {p2.name}, {p2.age}, {p2.address}")

print(p1) 
print(p2) 
print(type(p1)) 
print(type(p2)) 
print(p1 == p2)  # False, different instances