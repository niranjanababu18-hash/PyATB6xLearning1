class basecounter:
    def __init__(self):
        self.count = 0
    def counter(self):
        self.count += 1
        return self.count
class testexecution(basecounter):
    pass
t=testexecution()
t.counter()
t.counter()
t.counter()
print(t.counter())



