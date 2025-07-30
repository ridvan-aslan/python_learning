#key - value

# 41 => Kocaeli
# 34 => Istanbul

cities = ["Kocaeli", "Istanbul"]
plates = [41, 34]

# print(plates[cities.index("Istanbul")])

plates_dict = {
    "Kocaeli": 41,
    "Istanbul": 34
}

# print(plates_dict["Istanbul"])
# print(plates_dict["Kocaeli"])

plates_dict["Ankara"] = 6
plates_dict["Kocaeli"] = "New value"

# print(plates_dict)

users = {
    "Rıdvan": {
        "age": 22,
        "roles": ["admin", "user"],
        "city": "Tekirdag",
        "phone": "000-000-0000",
        "email": "ridvan_example_gmail.com"
        
    },
    "Ali": {
        "age": 30,
        "roles": ["user"],
        "city": "Kocaeli",
        "phone": "000-000-0000",
        "email": "ali_example_gmail.com"
    }
}

print(users["Rıdvan"]["age"])
print(users["Ali"]["city"])
print(users["Rıdvan"]["roles"][0])
print(users["Ali"]["roles"][0])