import os

if os.path.exists("Bala1.txt"):
    print("File exists")
else:
    file = open("Bala1.txt","x")
    print("file created")
    file.close()

if os.path.exists("Bala1.txt"):
    os.remove("Bala1.txt")
    print("File deleted successfully")
else:
    print("File does not exist")

