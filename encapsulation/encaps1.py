class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def getBalance(self):
        print("Balance:", self.__balance)


account = BankAccount(1200000)

#account.__balance = 120000000
account.deposit(100000)
account.getBalance()
