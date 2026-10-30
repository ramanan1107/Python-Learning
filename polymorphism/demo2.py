class ClassA:
    def add(self,a,b):
        return a+b

class ClassB(ClassA):
    def add(self,a,b):
        return a-b

c = ClassB()
res = c.add(30,20)
print(res)
