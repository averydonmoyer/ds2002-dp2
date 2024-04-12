#!/home/gitpod/.pyenv/shims/python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.nem2p
collection = db.pyimport

path = "."

for (root, dirs, file) in os.walk(path):
    for f in file:
        with open(f) as jsf:
            try:
                file_data = json.load(jsf)
            except Exception as e:
                print("A JSON error occurred ::", e)
                continue
        if isinstance(file_data, list):
            try:
                collection.insert_many(file_data)
            except pymongo.errors.JSONDecodeError as e:
                print("Error decoding JSON ::", e)
                continue
            except Exception as e:
                print("An exception occurred ::", e)
                continue
        else:
            try:
                collection.insert_one(file_data)
            except Exception as e:
                print("An exception occurred ::", e)
                continue