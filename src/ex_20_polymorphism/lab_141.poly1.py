#same function can be multiple behavior
#method overriding
#method overloading
class basetest:
    def run(self):
        print("base method")
class logintest(basetest):
    def run(self):
        print("login test")

t=logintest()
t.run()
