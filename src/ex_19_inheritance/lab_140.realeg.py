class basetest:
    def __init__(self,browser):
        self.browser=browser
    def setup(self):
        print(f"launching {self.browser}")
class logintest(basetest):
    def run(self):
        self.setup()
        print("Running login test")
class signuptest(basetest):
    def run(self):
        self.setup()
        print("Running signup test")

test=logintest("chrome")
test.run()
test1=signuptest("firefox")
test1.run()
