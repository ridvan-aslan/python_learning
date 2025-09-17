import pymongo
from dotenv import load_dotenv
import os

load_dotenv()


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]

mycollection = mydb["products"]

# product = {"name": "Samsung S10", "price": 4000}

# result = mycollection.insert_one(product)

# print(result)
# print(result.inserted_id)

products = [
    {"name": "Samsung S8", "price": 3000, "description": "good phone"},
    {"name": "Samsung S7", "price": 2000, "categories": ['phone', 'tablet']},
]

result = mycollection.insert_many(products)

print(result.inserted_ids)