class basetest:
    def setup(self):
        print("base setup")
    def run(self):
        print("base run")
class logintest(basetest):
    def run(self): #oveririding
        print("login run")
class signuptest(basetest):
    def run(self):#overriding
        print("signup run")
t=basetest()
t.run()
#object created method will run
