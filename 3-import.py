from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json


MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# define database and collection 
db = client["hdj3fw"]

db.create_collection("dp2_files") 

collection = db.dp2_files


directory = "data"

for filename in os.listdir(directory):
  with open(os.path.join(directory, filename)) as f:
    print(f)
    # do other things with f

def get_files(): 
    try: 
        for _ in range(50): 
            file_data = json.load(f)

            if isinstance(file_data, list):
                try:
                    collection.insert_many(file_data)
                except Exception as e:
                    print(e, "when importing into Mongo")
            else:
                try:
                    collection.insert_one(file_data)
                except Exception as e:
                    print(e)
                    continue 

    finally: 
        pass 

# call the function 
if __name__ == "__main__": 
    get_files() 