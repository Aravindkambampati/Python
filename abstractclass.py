from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def add(self):
        pass
class Calculator(BaseClass):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b

obj = Calculator(3,2)
print(obj.subtract())