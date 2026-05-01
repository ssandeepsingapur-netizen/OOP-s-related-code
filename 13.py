class bank:
    def __init__(self,bank_name,holder_name,balance_amount,deposite):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.balance_amount = balance_amount
        self.deposite = deposite
    
    def check_balance(self):
        print("remainin balance is :",self.balance_amount)


    def deposit(self):
        if self.balance_amount >= 10000:
            total_amount = self.balance_amount+self.deposite
            print(total_amount)
       
    

B1 = bank("SBI","sandeep",12000,2000)
B1.check_balance()
B1.deposit()



