#Without parameter without return
def welcome():
    print("Hi, everyone")
    print("Welcome")
    print("Thanks for comming")
#With parameter without return
def sum1(a,b):
    print(a+b)
#Without parameter with return
def prod():
    a = 7
    b = 20
    c = a*b
    return c

#With parameter with return
def square(a):
    res = a*a
    return res
welcome()
#a = 10
#b = 20
sum1(10,20)

value = prod() + 50
print(value)

value2 = square(7)
print(value2)



