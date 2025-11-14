class person:
    name=None
    age=None
    height=None
    weight=None
    place=None

    def __init__(self, name, age, height, weight, place):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.place = place
    def nameofperson(self):
        print(self.name)
    def heightofperson(self):
 #       print("height is :",self.height)
        return self.height
    def ageofperson(self):
 #       print("age is :",self.age)
        return self.age
    def weightofperson(self):
 #      print("weight is :",self.weight)
       return self.weight
    def placeofperson(self):
        return self.place


abc=person("Niranjana",30,156,58,"payyanur")
abc.nameofperson()
print("height of person is ",abc.heightofperson())
print("age is ",abc.ageofperson())       # note the () to call the function
print("weight is ",abc.weightofperson())    # note the () to call the function
print("place is ",abc.placeofperson())

