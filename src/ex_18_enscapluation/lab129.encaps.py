import os
from dotenv import load_dotenv
#we are using credentials available env fle
class VMOLOGINPAGE:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        if self.email==os.getenv("email") and self.password==os.getenv("password"):
            print("allowed to login")
        else:
            print("login denied")
email=input("enter your email")
password=input("enter your password")
vom_object_ref=VMOLOGINPAGE(email,password)
vom_object_ref.login_confirm()
