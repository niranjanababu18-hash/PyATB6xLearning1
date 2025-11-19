class car:
    def __init__(self):
        self.password="Niranjana"
        self.__password_secure="pass123"
        #__private variable
    def nany(self):
        self.__password_secure="345"
        #private variables can only be ensacpulated within method and accesssed only via method
obj_ref=car()
obj_ref.nany()
