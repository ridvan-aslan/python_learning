import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()

for i in mycollection.find({}, {"_id": 0, "name": 1, "price": 1}):
    print(i)


# print(result)
