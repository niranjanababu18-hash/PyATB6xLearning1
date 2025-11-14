class calc:
    a=None
    b=None
    def __init__(self,a,b):
        print("DC")
        self.a=a
        self.b=b
    def sum(self,a,b):
        return a+b

a=int(input("enter first number"))
b=int(input("enter second number"))
s=calc(a,b)
print(s.sum(a,b))
