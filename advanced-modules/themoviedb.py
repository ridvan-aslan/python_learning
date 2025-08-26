import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Movie:
    def __init__(self):
        self.api_key = os.getenv("MY_MOVIE_API")
        self.api_url = "https://api.themoviedb.org/3/authentication"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
            }
        self.base_url = "https://api.themoviedb.org/3"
        
    def get_movies(self, movie_name):
        response = requests.get(f"{self.base_url}/search/movie", headers=self.headers, params={"query": movie_name, "language": "tr-Tr"})
        
        return response.json()
    
    def popular_movies(self):
        response = requests.get(f"{self.base_url}/movie/popular", headers=self.headers, params={"language": "tr-Tr"})

        return response.json()
    
    def upcoming_movies(self):
        response = requests.get(f"{self.base_url}/movie/upcoming", headers=self.headers, params={"language": "tr-Tr"})

        return response.json()

movie = Movie()

while True:
    choice = input("1- Find Movie\n2- Popular Movies\n3- Upcoming Movies\n4- Exit\nEnter your choice: ")    
    
    if choice == "4":
        print("Exiting...")
        break
    elif choice == "1":
        movie_name = input("Enter the name of the movie: ")
        for movie_item in movie.get_movies(movie_name)["results"]:
            print(movie_item["title"])
    elif choice == "2":
        for movie_item in movie.popular_movies()["results"]:
            print(movie_item["title"])
    elif choice == "3":
        for movie_item in movie.upcoming_movies()["results"]:
            print(movie_item["title"])
    else:
   
       print("Invalid choice. Please try again.")
  



