class animal:
    def dog(self):
        print("dog is barking")
    def cat(self):
        print("cat is meowing")
class pet(animal): #inheritance
    def rabbit(self):
        print("rabbit is hopping")

p1 = pet()
p1.dog()
p1.cat()
p1.rabbit()