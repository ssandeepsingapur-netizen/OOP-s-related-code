class Animal:
    def speak(self):
        print("animal makes sound")

class dog(Animal):
    def bark(self):
        print("Dog barks")

d = dog()
d.speak()
d.bark()

