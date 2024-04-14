# Data Project 2: Import JSON to MongoDB

In this data project you will write a single file of code to import a bundle of fifty (50) separate JSON files into a new collection within a MongoDB database.

The script you write should import all files when executed only once. You should not need to run the script 50 separate times to import all files.

The data for import can be found in the `data/` directory of this repository.

Follow the steps below carefully and create a solution of your own.

## 1. Fork this Repository and open in Gitpod

Fork this repo so that you are working with your own copy of the code and can add, commit, and push freely. You will be submitting the URL to your fork for grading.

Open your repository in Gitpod by appending `https://gitpod.io/#` before the GitHub URL.

## 2. Choose Your Code

You are free to write this assignment in a `bash` script using a CLI tool called `mongoimport`, in Python using `pymongo`,
or both.

## 3. Connecting to MongoDB Atlas

See [this page](https://canvas.its.virginia.edu/courses/105117/pages/mongodb-credentials) in Canvas for how to set up connection credentials if you need them.

DO NOT commit the password to your GitHub repository!

For command-line access to MongoDB you have `MONGO-ATLAS` as an available command pre-built into your Gitpod configuration.

### Python in Gitpod

If using Python in Gitpod you already have the `MONGOPASS` environment variable and can then connect to a db/collection in Atlas using this code:

```
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.<db-name>
# specify a collection
collection = db.<collection-name>
```

- [`pymongo` documentation](https://pymongo.readthedocs.io/en/stable/)


### `mongoimport` in Gitpod

If using `mongoimport` within a `bash` script in Gitpod, you can create a new Gitpod User Variable with your full URI.

For instance, you could create a new variable named `MONGODB` with a value of `mongodb+srv://nmagee:xxxxxxxxxxx@cluster0.pnxzwgz.mongodb.net/<YOUR-DB>`

Note that you should replace the `xxxxxx` with the actual password, and replace `<YOUR-DB>` with the name of your MongoDB database. **Your URI must specify a database at the end.**

Then you can call this URI within a terminal command to connect automatically each time you use it like this:

```
mongoimport --uri $MONGODB --collection test  data.json --jsonArray
```

## 4. Listing Directory Contents

It is up to you to determine how you want to import the fifty files within `data/`. But here are some methods you might want to draw from:

### `bash`

In `bash` you can traverse a directory's contents, item by item:

```
for file in data/*
do
  echo "$file"
done
```

This means that each file name, in the course of each for-loop, becomes a variable you can use or pass to other code or commands.

For instance, this version of the above code would pass the file name of each file into a separate Python script:

```
for file in data/*
do
  /usr/bin/python3 my-import-script.py $file
done
```

### Python

In Python you can also traverse a directory's contents, item by item:

```
import os

path = "data"

for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)
```

## 5. Importing

### `mongoimport` with `bash`

To import a single JSON file into MongoDB using `mongoimport` use this syntax:

```
mongoimport --uri $MONGODB --collection test data.json --jsonArray
```

Note these details:

- The DB name should already be specified as part of the URI you created above.
- The collection should be specified in the command. You can create a new collection by simply naming it here.
- The data file itself is then passed.
- Finally, you must indicate that you are passing in a `--jsonAarray` for the command to succeed.

- [`mongoimport` documentation](https://www.mongodb.com/docs/database-tools/mongoimport/)

### `pymongo` in Python

To import a single JSON file into MongoDB using `pymongo` in a Python script use this syntax:

```
# assuming you have defined a connection to your db and collection already:

# Loading or Opening the json file
with open('data.json') as file:
    file_data = json.load(file)
     
# Inserting the loaded data in the collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
    collection.insert_many(file_data)  
else:
    collection.insert_one(file_data)
```

- [`pymongo` documentation](https://pymongo.readthedocs.io/en/stable/)


## 6. Error Handling

You may encounter an error when importing this stack of files. Your code should be able to handle this without breaking. You do not need to log your errors but your code should continue processing additional files.

Remember to assess where in your flow the errors occur, and handle them accordingly at each/any/every point with separate handlers as needed.

If you cannot elegantly handle the errors you may want to change your approach, or even your programming language.

## 7. Testing / Clearing Your Collection

As you test your code, MongoDB will not allow you to re-import files that have already been imported. To drop the collection to test again, open `mongosh` by typing `MONGO-ATLAS` in the Gitpod terminal.

Then:
```
use nem2p               # specify your database name
db.COLLECTION.drop()    # where COLLECTION is the name of your collection
```

## 8. Import Count

After successfully importing all complete records contained in all the files, determine how many documents have been imported into your collection. You may want to compare this against an actual count of complete, individual JSON records in the `data/`directory. (This may require a little bit of side coding of its own!)

- complete documents have been imported into your collection
- complete documents that could not be imported
- corrupted documents exist in the fileset 

Note the number of records you can successfully import in a file named `count.txt` and add it to your repository.

## 9. Submit

Add, commit, and push your working script and the `count.txt` file to your fork of the repository.

Submit the GitHub URL of your fork for grading.