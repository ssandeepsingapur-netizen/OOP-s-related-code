class Bird:
    def fly(self):
        print("Bird flies")

class Penguin:
    def fly(self):
        print(" Penguini can't fly")

for obj in (Bird(),Penguin()):
    obj.fly()