from abc import ABC, abstractmethod
class excelreader(ABC):
    @abstractmethod
    def readfromexcel(self):
        pass
class browser(excelreader):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class testcase(browser):
    def readfromexcel(self):
        print("read url")
    def start(self):
        print("start driver")
    def stop(self):
        print("stop driver")
    def run(self):
        self.readfromexcel()
        self.start()
        self.stop()
tc=testcase()
tc.run()
