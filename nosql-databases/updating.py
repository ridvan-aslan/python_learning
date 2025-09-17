import pymongo
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.update_one({"name": "Samsung S8"}, {"$set": {"name": "Samsung S8 II", "price": 3500}})
mycollection.update_many({"name": "Samsung S7"}, {"$set": {"name": "iPhone 15", "price": 15000}})

print(f"{mycollection.modified_count} documents updated.")

result = mycollection.find()

for i in result:
    print(i)


