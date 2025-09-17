import pymongo
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.delete_one({"name": "Samsung S8 II"})
# mycollection.delete_many({"name": {"$regex": "^S"}})

result =  mycollection.delete_many({})

print(f"{result.deleted_count} documents deleted.")

result = mycollection.find()

for i in result:
    print(i)


