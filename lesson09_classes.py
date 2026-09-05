"""
Lesson 9: Classes & Objects (OOP)

Demonstrates defining a class with a constructor (__init__), instance
attributes, and methods - then creating multiple independent objects
from the same class blueprint.
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, grade {self.grade}.")

    def has_passed(self):
        return self.grade in ["A", "B", "C"]

student1 = Student("Abdalla", 20, "A")
student2 = Student("Sara", 19, "F")

student1.introduce()
student2.introduce()

print(student1.has_passed())
print(student2.has_passed())
