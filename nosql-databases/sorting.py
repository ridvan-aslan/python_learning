import pymongo
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]
mycollection = mydb["products"]

result = mycollection.find().sort("name", -1)
result = mycollection.find().sort("price", -1)
result = mycollection.find().sort([("name", 1), ("price", -1)])

for i in result:
    print(i)


