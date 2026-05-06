from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def star(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")



C = Car()
C.start()