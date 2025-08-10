# Inheritance 

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person constructor called")

    def who_am_i(self):
        return f"I am a person"
    
    def eat(self):
        return "I am eating"

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.student_number = number

        print("Student constructor called")
    
    # Override the who_am_i method
    def who_am_i(self):
        return f"I am a student"
    
    def sayHello(self):
        return "Hello from Student class"
    
class Teacher(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject

        print("Teacher constructor called")
    
    def who_am_i(self):
        return f"I am a {self.subject} teacher"
    
    

p1 = Person("Rıdvan", "Aslan")
s1 = Student("Ali", "Yılmaz", 12345)  

print(f"Person: {p1.fname} {p1.lname}")
print(f"Student: {s1.fname} {s1.lname} with number {s1.student_number}")

print(p1.who_am_i())
print(s1.who_am_i())

print(p1.eat())
print(s1.eat())

print(s1.sayHello())

t1 = Teacher("Rıdvan", "Aslan", "Software Development")
print(f"Teacher: {t1.fname} {t1.lname} teaches {t1.subject}")