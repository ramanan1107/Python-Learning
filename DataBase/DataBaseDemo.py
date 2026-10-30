from pymongo import MongoClient
server = MongoClient("mongodb://localhost:27017/") #Server
db = server["PythonRockers"] #Database
collection1 = db["Students"] #Collection
student1 = {
                    "name":"Ramanan",
                    "rollNo":169,
                    "phno":9876543210
                    }

students = [{
     "name":"Sathana",
     "rollNo":77,
     "phno":9876543210
     },
    {
      "name":"Visubaala",
      "rollNo":47,
      "phno":9876543210
     },
     {
      "name":"Aishwarya",
      "rollNo":39,
      "phno":9876543210
     }
    ]
#output = collection1.insert_one(student1)
#print("Inserted ID:", output.inserted_id)
#collection1.insert_many(students)
collection1.update_many(
    {"name":"Ramanan"},
    {"$set" :{"phno":9025922054}}
     )

server.close()



