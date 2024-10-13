from abc import ABC,abstractmethod
#abstract method
class Declare(ABC):
    def declare(self):
        pass
    
class First(Declare):
    def declare(self):
        print("first classs is implemented using declare")
        
first= First()
first.declare()
    