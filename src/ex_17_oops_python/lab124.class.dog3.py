#constructors are used to initialize values of attributes

class Dog:
    name=None
    height=None
    weight=None
    breed=None

    def walk(self):
        print(self.name)
    def sleep(self):
        print(self.breed)

    def __init__(self,namegiven,breedgiven):
        self.name=namegiven
        self.breed=breedgiven

chow=Dog(namegiven="chow",breedgiven="chow")
chow.walk()
ranco=Dog(namegiven="ranco",breedgiven="ranco")
ranco.sleep()


