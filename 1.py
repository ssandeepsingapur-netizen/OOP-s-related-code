class Bankaccount:
    def __init__ (self, name, balance=0):
        self.name = name
        self__balance = balance #private

    def deposite(self,amount):
        self.balance = amount
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")

    def show__balance(self):
        print(self.balance)

acc1 = Bankaccount("sandeep",10000)
acc1.deposite(500)

    
