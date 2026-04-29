class mobile:
    def __init__ (self,name,brand):
        self.name = name
        self.brand = brand

    def display_info(self):
        print(f"mobile name is {self.name} and brand is {self.brand}")

m1 = mobile("redmi","android")
m1.display_info()