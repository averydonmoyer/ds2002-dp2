from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

# connect to MongoDB 
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='hdj3fw', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# define database and collection 
db = client.hdj3fw
collection = db.dp2_test

directory = "data/" 

# write the loop  
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f: 
        try: 
            file_data = json.load(f)
            if isinstance(file_data, list):
                try: 
                    collection.insert_many(file_data)
                    print(f, " successfully imported")
                except Exception as e:
                    print(e, "when importing file")
                    continue 
            else:
                collection.insert_one(file_data)
        except Exception as e:
            print(e, " when loading file ", f) 
        finally: 
            pass 