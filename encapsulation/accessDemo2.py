class Student:
    def __init__(self):
        self.__name = "Visubaala"

    def display(self):
        print(self.__name)

s1 = Student()
s1.display()
print(s1.__name)
