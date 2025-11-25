class utility:
    @staticmethod
    def greet(name):
        print("hi",name)
    def greet_personal(self,name):
        self.name=name
        print("hi",self.name)
utility.greet("Jim")
t=utility()
t.greet_personal("Jimboy")
