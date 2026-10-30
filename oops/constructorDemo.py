class MyClass:
    def __init__(self,name,age,dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Dept: ",self.dept)

mc1 = MyClass("Ramanan",18,"IT")
mc2 = MyClass("Srinivasan",20,"CSE")

#print(mc1)
mc1.display()
mc2.display()
"""print(mc1.name)
print(mc1.age)
print(mc1.dept)

print(mc2.name)
print(mc2.age)
print(mc2.dept)"""

