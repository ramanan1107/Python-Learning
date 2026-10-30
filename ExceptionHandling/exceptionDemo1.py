a = 10
b = 2
name = "Swetha"
myList = [97,99,98,94,97]

try:
    c= a/b
    prin(c)
    myList[10]
except ZeroDivisionError:
    print("Cant divide by zero")
except IndexError:
    print("Can only access index with in range")
else:
    print("No Exception")
finally:
    print("This will always work")
print("Hello")



#try, except, finally,else
