import functools
#Map
def bonus(mark):
    return mark+2

ramMarks = [97,98,96,95,89]

result = map(bonus,ramMarks)
print(list(result))

##ramMarks = [97,98,96,95,89]
##dummy = []
##
##for mark in ramMarks:
##    dummy.append(mark+2)
##
##print(dummy)

#Filter
def check(x):
   return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = filter(check, numbers)
print(list(result))

#Reduce
myList = [10,20,30,40,50]
def add (a,b):
    return a+b

res = functools.reduce(add,myList)
print(res)




