#hybrid
#mixture of mutilevel and multiple and hierarchial
class Base:
    def base_method(self):
        print("base method")
class A(Base):
    def firstmethod(self):
        print("first method")
class B(Base):
    def secondmethod(self):
        print("second method")
class C(A,B):
    def thirdmethod(self):
        print("third method")
test=C()
test.base_method()
test.firstmethod()
test.secondmethod()
test.thirdmethod()
