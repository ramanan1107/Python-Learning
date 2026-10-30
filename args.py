def add(a,*numbers,b):
    print(numbers)
    print(a)
    print(b)

add(10,20,30,40,50, b = 60)

def demo(name,age):
    print("Name",name)
    print("Age",age)

demo(age = 20,name = "Ramanan")

def demo2(**value):  #key value
    print(value)
    print(value["name"])

demo2(age = 21, name = "Akash")



