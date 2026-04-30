class market:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def Get__info(self):
        if self.stock >= 50:
            print(self.name)
            print(self.price)
        elif self.stock <=25:
            print(self.name)
            print(self.price*2)
        elif self.stock == 0:
            print("no product at this time")

m1 = market("apple",50,60)
m1.Get__info()
