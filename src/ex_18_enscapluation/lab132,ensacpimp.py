class Home:
    def __init__(self):
        self.public_var="father"
        self.__private_var="baby"
        self._protected="brother"
        #_-protected
    def mom(self):
        print(self.__private_var)
        self.__wife()
        print(self._protected)
        #not recommended to use protected in python
    def __wife(self):
        print(self.__private_var)

obj_ref=Home()
obj_ref.mom()
print(obj_ref.public_var)
