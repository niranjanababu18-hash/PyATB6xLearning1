from abc import ABC,abstractmethod
class father(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass
class son(father):
    def loan(self):
        print("Son is paying loan of amount of 50k")
amit=son("AMIT")
amit.loan()