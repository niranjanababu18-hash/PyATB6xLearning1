print("outside")
class mobile_phone:
    model=None
    def __init__(self):
        print("constructor")

    def talk(self):
        print("talk")
print("outside2")
#creating object and calling method
iphone=mobile_phone()
iphone.talk()

