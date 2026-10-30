a=int()
b=int()
c=int()
try:
    a = int(input("Enter the mark 1:"))
    b = int(input("Enter the mark 2:"))
    c = int(input("Enter the mark 3:"))
except ValueError:
    print("Please enter valid numeric marks")
if (a or b or c <0 )and (a or b or c >100):
    raise Exception("Marks must be between 0 and 100")
else:
    d=a+b+c
    print(d/3)
