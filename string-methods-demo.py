website = "https://www.google.com/"
course = "Python Programming: A Complete Beginner to Advanced Guide"

result = "  Hello, World!  "

# print(result.strip())  
# print(result.lstrip())  
# print(result.rstrip())
# print(website.strip("htps:/w.com"))


# print(course.lower()) 
# print(course.upper())
# print(course.title())
# print(course.capitalize()) 

# print(website.count("o"))
# print(website.count("o" , 0, 15))  

# print(website.find("google"))  
# print(website.find("google" , 0, 25))  
# print(website.rfind("g"))  

# print(website.index("google"))
# print(website.index("googlee"))  # Raises ValueError if not found


# print(website.startswith("https://"))
# print(website.endswith(".com"))

# print(course.isalpha())  
# print(course.isdigit())  

message = "Contents"

# print(message.center(50, "*"))  
# print(message.ljust(50, "*"))  
# print(message.rjust(50, "*"))  

# print(course.replace(" " , "-"))
# print(course.replace(" " , "-",5))
# print(website.replace("https://", "").replace("/", "")) 
# print(result.replace("World" , "There"))

print(course.split(" "))