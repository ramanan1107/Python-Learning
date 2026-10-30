##m1 = 99
##m2 = 100
##m3 = 65
##m4 = 75
##m5 = 60
##m6 = 99

marks = [99,100,65,75,60,99]

data = ["John", 25, 5.8, True]
             #0     1   2   3   4   5

##temp = marks
temp = marks.copy()
marks.append(79)
marks.insert(3,89)
marks.extend([99,85,67])
print(marks)
print(marks[3]) 
print(temp)
