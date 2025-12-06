from abc import abstractmethod,ABC
class Universitet(ABC):
    def __init__(self,id,name,age):
        self.__id=id
        self.name=name
        self.age=age
    @abstractmethod
    def get_info(self):
        pass
    def privet_id(self):
        return self.__id
class Student(Universitet):
    def get_info(self):
        return f"{self.privet_id()} {self.name} {self.age}"

uquvchi=Student(12,'Elshodbek',16)
print(uquvchi.get_info())
print('salom')