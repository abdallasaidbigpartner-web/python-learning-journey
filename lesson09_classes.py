"""
Lesson 9: Classes & Objects (OOP)

Demonstrates defining a class with a constructor (__init__), instance
attributes, and methods - then creating multiple independent objects
from the same class blueprint.

Refactored (Phase 4 - Software Engineering) to add type hints, input
validation, and method-level docstrings - professional practices that
make code more robust and self-documenting.
"""


class Student:
    """Represents a student with a name, age, and letter grade."""

    VALID_GRADES = ["A", "B", "C", "D", "F"]

    def __init__(self, name: str, age: int, grade: str):
        if age <= 0:
            raise ValueError("Age must be a positive number")
        if grade not in self.VALID_GRADES:
            raise ValueError(f"Grade must be one of {self.VALID_GRADES}")

        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self) -> None:
        """Print a short introduction of this student."""
        print(f"Hi, I'm {self.name}, {self.age} years old, grade {self.grade}.")

    def has_passed(self) -> bool:
        """Return True if the student's grade counts as passing (A-C)."""
        return self.grade in ["A", "B", "C"]


student1 = Student("Abdalla", 20, "A")
student2 = Student("Sara", 19, "F")

student1.introduce()
student2.introduce()

print(student1.has_passed())
print(student2.has_passed())

# Validation check: this should raise an error, proving our validation works
try:
    invalid_student = Student("Test", -5, "A")
except ValueError as e:
    print(f"Validation caught an error as expected: {e}")
