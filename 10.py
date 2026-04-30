class BankAccount:
    def __init__(self,name,Houlder_name,id,balance,rate,time):
        self.name = name
        self.Houlder_name = Houlder_name
        self.id =id
        self.__balance = balance
        self.rate = rate
        self.time = time
    
    def balance_info(self):
        print(self.__balance)
        if self.__balance >=10000:
            print("You eligigible for loan")
            p = (self.__balance*self.rate*self.time)/100
            print(p)
        else:
            print("your not eligible for loan")

    

b1 = BankAccount("SBI","sandeep",123,20000,2,2)
b1.balance_info()