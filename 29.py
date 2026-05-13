class bank:
    def __init__(self, __balance):
        self.__balance = __balance
        print("intial balnce is ", self.__balance)

    def deposite(self,amount):
        self.__balance += amount
        print("total amount is", amount)

    def showbalance(self):
        print("total balance is ", self.__balance)


b1 = bank(1000)
b1.deposite(500)
b1.showbalance()
