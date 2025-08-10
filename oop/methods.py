# # class

# class Person:
#     pass # "pass" is a placeholder

#     # class attributes    
#     address = "Unknown"  

#     # constructor
#     def __init__(self, name, age):
#         # object attributes
#         self.name = name
#         self.age = age
#         print("Person created:", self.name, self.age)

#     # instance methods
#     def intro(self):
#         print("Hello my name is", self.name, "and I am", self.age, "years old.")

# # object, instance

# p1 = Person(name = "Alice", age =30) 
# p2 = Person("Bob", 25)

# p1.intro()  

class Circle:
    # class attribute
    pi = 3.14

    # constructor
    def __init__(self, radius = 1):
        self.radius = radius

    # instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * Circle.pi * self.radius
    
c1 = Circle(5)
c2 = Circle()

print("Area of circle:", c1.area())
print("Circumference of circle:", c1.circumference())

print("Area of default circle:", c2.area())
print("Circumference of default circle:", c2.circumference())