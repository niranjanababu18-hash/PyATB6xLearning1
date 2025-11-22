#hierararical inheritance.one father so many childs
class basetest:
    def setup(self):
        print("Father")
class logintest(basetest):
    def login(self):
        print("Iam child1")
class UItest(basetest):
    def UItest(self):
        print("Iam child2")
login=logintest()
ui=UItest()
login.setup()
login.login()
ui.UItest()