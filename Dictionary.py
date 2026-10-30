#mySet = {10,20,30,20}
mySet = set()
print(type(mySet))

myDict = {"name":"Swetha",
                "age":20,
                "country":"USA"}
myDict["city"] = "Pondicherry"
myDict["country"] = "Canada"
print(myDict)
print(myDict["name"])

for key,value in myDict.items():
    print(key,value)
myDict["country"] = "London"
print(myDict)

