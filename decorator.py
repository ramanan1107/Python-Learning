"""def car (namanan):
    print("1. Car taken")
    def modification():
        namanan()
        print("3.Modification started")
        print("4.Modification Ended")
    return modification
@car
def onprocess():
    print("Onprocess")
print("2.Arrived to the shed")
onprocess()

def decor(func):
    count = [0]
    def wrapper():
        count[0] += 1
        print("Function called", count[0], "time(s)")
        func()
    return wrapper
@decor
def hello():
    print("Hello")
hello()
hello()
hello()"""


def first(func):
    def wrapper():
        print("First Start")
        func()
        print("First End")
    return wrapper
def second(func):
    def wrapper():
        print("Second Start")
        func()
        print("Second End")
    return wrapper
@first
@second
def hello():
    print("Hello")
hello()

    
