#person
class person:
    name=None
    age=None
    def __init__(self,name,age):
        self.name=input("enter the name")
        self.age=input("enter the age")
#    def display(self):
#        print(self.name,self.age)
    def display_values(self):
        print("Name is ",self.name,"Age is ",self.age)
amit=person("amit",25)
amit.display_values()
