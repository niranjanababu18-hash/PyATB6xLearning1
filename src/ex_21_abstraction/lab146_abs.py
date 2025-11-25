#import ABC CLASS AND ABSTRACTMETHOD DECORATOR FROM abc module
from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Animal barking with name as ",self.name)
dog=Dog("tinto")
dog.sound()