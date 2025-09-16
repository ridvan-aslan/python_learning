import pymongo
from dotenv import load_dotenv
import os

load_dotenv()


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(os.getenv("MONGO_CONNECTİON"))

mydb = myclient["node-app"]

print(myclient.list_database_names())
