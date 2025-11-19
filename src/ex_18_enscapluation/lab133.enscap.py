class test:
    def __init__(self):
        self.driver="chrome"#public
        self._config="env"#protected
        self.__api__key="ABC78#"#private
    def show(self):
        print(f"driver is {self.driver}")
        print(f"config is {self._config}")
        print(f"api key is {self.__api__key}")
ob_ref=test()
ob_ref.show()
#print(ob_ref.__api__key)
