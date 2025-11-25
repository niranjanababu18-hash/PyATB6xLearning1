class excelreader:
    @staticmethod
    def readexcel():
        print("read excel")
class mysqlconnection:
    @staticmethod
    def readmysql():
        print("read mysql")
class tc1:
    def run(self):
        #calling directly static method
        excelreader.readexcel()
        mysqlconnection.readmysql()
t=tc1()
t.run()