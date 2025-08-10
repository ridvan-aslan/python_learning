my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"

print(len(my_list))
print(len(my_string))

print(type(my_list))
print(type(my_string))

class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie object created")

    def __str__(self):
        return f"Movie: {self.title}, Director: {self.director}, Duration: {self.duration} minutes"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print(f"Movie '{self.title}' deleted")

m = Movie("Movie Title", "Director Name", 120)

print(str(m))
print(str(my_list))

print(len(m)) 

