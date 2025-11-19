class bank:
    def __init__(self,account_number,balance):
        self.balance=balance
        self.__account_number=account_number

    def deposit(self,amount):
        self.balance=self.balance+amount
    def showmeaccntnumber(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("not allowed")
icici=bank("34677899",100000)
icici.deposit(1000)
print(icici.balance)
icici.showmeaccntnumber(True)
print(icici.showmeaccntnumber)

