"""a = 10
b = 0

c = a/b"""

"""num = 10

if num>=9:
    raise ZeroDivisionError()"""

class InvalidAgeException(Exception):
    pass



def ageValidator(age):
    if age<18:
        raise InvalidAgeException("Not eligible, age should be 18 or above")

age = int(input("Enter your age: "))
ageValidator(age)






