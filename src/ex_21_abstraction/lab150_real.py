from abc import ABC, abstractmethod
class gearbox(ABC):
    @abstractmethod
    def  setgear(self):
        pass
class engine:
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car(engine,gearbox):
    def setgear(self):
        print("start gear")
    def start(self):
        print("start the engine")
    def stop(self):
        print("stop the engine")
    def drive(self):
        self.start()
        self.stop()
        self.setgear()
veh=car()
veh.drive()