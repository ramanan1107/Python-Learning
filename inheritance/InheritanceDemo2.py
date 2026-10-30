class GrandFather:
    def __init__(self):
        self.money = 20000

class Father(GrandFather):
    pass

class Son(Father):
    pass

f = Father()
s = Son()
print(f.money)
print(s.money)

    
