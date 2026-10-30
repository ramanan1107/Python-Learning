"""def sumOf(a,b):
    return a+b

value =  sumOf(10,20)
print(value +10)"""

def myFunc(a,b,name):
    print(a,b)
    print(name)

myFunc(10,"John",20)

def myFunc2(a,*numbers):   #*args  Positional arguments
    sum = 0
    for i in numbers:
        sum = sum+i 
    print(sum)
    print(a)

myFunc2(10,20,30,40,50)

"""def myFunc3(*strings):
    print(strings)

myFunc3("Hello","Hi",True,10)"""

def myFunc4(name,age):      
    print("Name:",name)
    print("Age:",age)

myFunc4(age = 19,name = "Ramanan") #Keyword arguments

def show_info(*args,**kwargs):
    print(kwargs)
    print(args)

show_info(10,20,30,40,name="John", age=25, city="London")


