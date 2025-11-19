class basetest:
    _driver="chrome"
    def setup(self):
        print("Launching browser:"+self._driver)
    def teardown(self):
        print("Closing browser")
class logintest(basetest):
    def run_test(self):
        print("Running login test with user: "+self.__username)
    def user(self):
        self.__username = "neenu"


obj_ref=logintest()
obj_ref.user()
obj_ref.setup()
obj_ref.run_test()
obj_ref.teardown()