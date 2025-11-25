class maths:
    #non static
    def division(self,a,b):
        return a/b
    #statis without self
    @staticmethod
    def add(a,b):
        return a+b
t=maths()
print(t.division(10,2))
print(t.add(2,3))