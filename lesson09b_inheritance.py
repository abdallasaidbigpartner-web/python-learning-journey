"""
Lesson 9b: Inheritance

Demonstrates a child class inheriting attributes/methods from a
parent class, overriding a method, and using super() to extend
(rather than fully replace) the parent's behavior.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        print(f"{self.name} earns {self.salary} per month.")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def describe(self):
        super().describe()
        print(f"{self.name} manages a team of {self.team_size}.")

employee1 = Employee("Sara", 2000)
manager1 = Manager("Abdalla", 4000, 6)

employee1.describe()
manager1.describe()
