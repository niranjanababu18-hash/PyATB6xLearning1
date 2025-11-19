#single inheritance
class basetest:
    driver = "chrome"
    __driver2="edge"
    def setup(self):
        print("setup")
        print("running>>" + self.__driver2)
class login(basetest):
    def run(self):
        self.setup()
        print("running>>"+self.driver)
      #  print("running>>" + self.__driver2)--.private cannot accessed into another class
t=login()
t.run()