from abc import ABC,abstractmethod

class Hotel(ABC):
    @abstractmethod
    def breakFast(self):
        pass

    @abstractmethod
    def lunch(self):
        pass

    @abstractmethod
    def dinner(self):
        pass

class Rolex(Hotel):
    def breakFast(self):
        print("Egg Dosa")

    def lunch(self):
        print("Mutton Biriyani")

    def dinner(self):
        print("Parotta with Chettinadu gravy")

r = Rolex()
r.breakFast()
r.lunch()
