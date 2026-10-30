from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection
mongoUrl = MongoClient("mongodb://localhost:27017")

myDB = mongoUrl["college"]
myCollection = myDB["Student_details"]


# 1. CREATE - Insert a new student
def createUser(user):
    data = myCollection.insert_one(user)

    print("Student created successfully")
    print("Inserted ID:", data.inserted_id)


# 2. READ - Get all students
def getUsers():
    data = myCollection.find()

    for user in data:
        print(user)


# 3. READ - Get a specific student using ID
def getSpecificUser(userId):
    data = myCollection.find_one({
        "_id": ObjectId(userId)
    })

    if data:
        print(data)
    else:
        print("Student not found")


# 4. UPDATE - Update student details using ID
def updateUser(userId, updatedData):
    data = myCollection.update_one(
        {"_id": ObjectId(userId)},
        {"$set": updatedData}
    )

    if data.matched_count > 0:
        if data.modified_count > 0:
            print("Student updated successfully")
        else:
            print("No changes were made")
    else:
        print("Student not found")


# 5. DELETE - Delete a student using ID
def deleteUser(userId):
    data = myCollection.delete_one({
        "_id": ObjectId(userId)
    })

    if data.deleted_count > 0:
        print("Student deleted successfully")
    else:
        print("Student not found")


# Sample student data
user1 = {
    "name": "Bala",
    "mobile": 922254210,
    "email": "bala@gmail.com",
    "address": "No:4, aaa street",
    "age": 22
}

user2 = {
    "name": "Ramanan",
    "mobile": 9336342101,
    "email": "ram@gmail.com",
    "address": "No:4, 123 street",
    "age": 18
}

user3 = {
    "name": "Srinivasan",
    "mobile": 975841631,
    "email": "sri@gmail.com",
    "address": "No:6, 123 street",
    "age": 21
}

# CREATE
#createUser(user3)


# READ ALL
#getUsers()

# READ ONE
#getSpecificUser("6ae20576be4179b65c0bb4a4")

# UPDATE
##updateUser(
##   "6ae20773ab9a3110e13a15d2",
##   {"address": "No:10, 123 street"}
##)

# DELETE
#deleteUser("6ae2072ef51e1dfcb397a1ff")

"""data = myCollection.find({
    "age":{"$eq":21}
    })

data = myCollection.find({
    "age":{"$gt":15}
    })

data = myCollection.find({
    "age": {"$in": [18, 21]}
    })

for temp in data:
  print(temp)

data = myCollection.find().sort("age", 1)

for student in data:
    print(student)
"""
##data = myCollection.find().sort("mark", -1)
##
##for student in data:
##    print(student)

data = myCollection.find().sort("mark", -1).limit(2)

for student in data:
    print(student)

