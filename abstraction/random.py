from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "course"])

s1 = Student("Arun", 21, "Python")

print(s1.name)
print(s1.age)
print(s1.course)
