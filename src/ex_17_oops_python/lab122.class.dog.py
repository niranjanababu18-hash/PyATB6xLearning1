class dog:
    name=None
    breed=None
    height=None
    weight=None

    def bark(self):
        print("bark")
        print(self.name)
# using self ,all atrributes can be accessed


print("outside")
#object of class
chow=dog()
#using same class name creating object.chow is a n object reference
rancho=dog()
