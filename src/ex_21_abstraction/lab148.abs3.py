from abc import ABC, abstractmethod
class browser(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("Browser stopped")
class runtest(browser):
    def start(self):
        print("Browser started")
test=runtest()
test.start()
test.stop()