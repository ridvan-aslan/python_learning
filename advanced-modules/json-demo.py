import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.current_user = None

        self.load_users()

    def load_users(self):
        if os.path.exists("advanced-modules/users.json"):
            with open("advanced-modules/users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    new_user = User(username = user["username"], password = user["password"], email = user["email"]) 
                    self.users.append(new_user)


    def register(self, user: User):
        self.users.append(user)
        self.save_to_file()
        print("User has been registered")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print("Logged in")
                return
            
        print("Invalid username or password")

    def identity(self):
        if self.current_user:
            print(f"Username: {self.current_user.username}\nEmail: {self.current_user.email}")
        else:
            print("You are not logged in")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out")
        else:
            print("No user is currently logged in")
    def save_to_file(self):
        my_list = [user.__dict__ for user in self.users]  

        with open("advanced-modules/users.json", "w", encoding="utf-8") as file:
            json.dump(my_list, file, ensure_ascii=False, indent=4)


repository = UserRepository()

while True:
    print("Menu".center(50, "-"))
    choice = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nEnter your choice: ")

    if choice == "5":
        print("Exiting...")
        break

    elif choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")

        user = User(username = username, password = password, email = email)
        repository.register(user)

    elif choice == "2":
        if repository.current_user:
            print("You are already logged in")
            continue
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        repository.login(username, password)    

    elif choice == "3":
        repository.logout()

    elif choice == "4":
        repository.identity()

    else:
        print("Invalid choice")

