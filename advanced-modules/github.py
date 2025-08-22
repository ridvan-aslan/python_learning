import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

my_token = os.getenv("MY_TOKEN")

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = my_token

    def get_user(self, username):
        response = requests.get(f"{self.api_url}/users/{username}")
        return response.json()
    
    def get_repos(self, username):
        response = requests.get(f"{self.api_url}/users/{username}/repos")
        return response.json()
    
    def create_repo(self, name):
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.post(
            f"{self.api_url}/user/repos",
            headers=headers,
            json={
                "name": name,
                "description": "açıklama",
                "homepage": "https://github.com",
                "private": False
            }
        )
        return response.json()
    


username = input("Enter username: ")
github = Github()

while True:
    choice = input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nEnter your choice: ")

    if choice == "4":
        print("Exiting...")
        break

    elif choice == "1":
        user = github.get_user(username)
        print(f"Name: {user['name']}, Public Repos: {user['public_repos']}, Followers: {user['followers']}")

    elif choice == "2":
        repos = github.get_repos(username)
        for repo in repos:
            print(repo["name"])

    elif choice == "3":
        repo_name = input("Enter repository name: ")
        new_repo = github.create_repo(repo_name)
        print(new_repo)

    else:
        print("Invalid choice")        
            