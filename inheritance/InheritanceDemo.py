class Father:
    money = 2000000

    def fatherFortune(self):
        print("Fortune worth 1500000")

class Son(Father):
    myMoney = 0

"""f = Father()
print(f.money)
f.fatherFortune()"""

s = Son()
s.myMoney = s.money
print(s.myMoney)
s.fatherFortune()
