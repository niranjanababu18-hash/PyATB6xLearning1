#ideally not possible in python just like java.but we can accomodate
class maths:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=3):
        return a+b+c
obj=maths()
obj.add(1,2)
print(obj.add(1.4,2.4))