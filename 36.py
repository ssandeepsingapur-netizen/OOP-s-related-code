class market:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  #private variable

    def display(self):
        print(f"Market Name: {self.name}")
        print(f"Balance: {self.__balance}")

m1 = market("Sandeep's Market", 10000)
    
m1.display()