#mutiple inheritance-not possible in java
class apibase:
    def apiauth(self):
        print("apiauth")
class dbbase:
    def dbauth(self):
        print("dbauth")
class test(apibase,dbbase):
    def run(self):
        self.apiauth()
        self.dbauth()
        print("test")
tc1=test()
tc1.run()

