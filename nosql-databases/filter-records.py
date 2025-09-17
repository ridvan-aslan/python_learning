import pymongo
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId


load_dotenv()


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]
mycollection = mydb["products"]


# result = mycollection.find_one(filter)
# result = mycollection.find_one({"_id": ObjectId("68c9cae1c44baca811cf95db")})
result = mycollection.find({"name": {"$in": ["Samsung S8", "Samsung S7"]}})
result = mycollection.find({"name": {"$regex": "^S"}})

result = mycollection.find({"price": {"$gte": 2000}})
result = mycollection.find({"price": {"$eq": 2000}})
result = mycollection.find({"price": {"$lte": 2000}})



for i in result:
    print(i)


