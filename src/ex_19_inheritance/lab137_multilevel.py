#multilevel inheritance--A->B->C
class testsuite:
    def info(self):
        print("Grandfather")
class Basetest(testsuite):
    def setup(self):
        print("Father")
class UItest(Basetest):
    def run(self):
        self.info()
        self.setup()
        print("child")
trun=UItest()
trun.run()