# global scope
x = "global x"

def myFunc():
    # local scope
    x = "local x"
    print("Inside myFunc:", x) 

myFunc()
print(x)

##########

name = "Rıdvan"

def change_name(new_name):
    name = new_name
    print(name)

change_name("Ali")
print(name)  # Output: Rıdvan

##########

name = "Global Name"

def greeting():
    # name = "Rıdvan"
    def say_hello():
        # name = "Ada"
        print("Hello", name)
    say_hello()

greeting() 

############

x = 50
def test():
    global x
    print("x is", x)  
    x = 2
    print("Changed x to", x)

test()  