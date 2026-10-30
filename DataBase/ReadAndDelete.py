from pymongo import MongoClient
server = MongoClient("mongodb://localhost:27017/") #Server
db = server["PythonRockers"] #Database
collection1 = db["Students"] #Collection

data = collection1.find()

for value in data:
    print(value)
