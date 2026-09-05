"""
Lesson 16: SOLID Principles (Liskov Substitution + Interface Segregation)

Demonstrates restructuring a class hierarchy so every subclass
genuinely fulfills its parent's contract (Liskov), and splitting a
broad interface into focused, role-specific ones (Interface
Segregation) rather than forcing unrelated behavior onto every class.
"""

from typing import Protocol


class Bird:
    """Base class - defines the general contract all birds share."""
    def move(self) -> str:
        raise NotImplementedError


class FlyingBird(Bird):
    def move(self) -> str:
        return "Flying"


class Penguin(Bird):
    def move(self) -> str:
        return "Swimming"


class Workable(Protocol):
    def work(self) -> str:
        ...


class Eatable(Protocol):
    def eat(self) -> str:
        ...


class Human:
    def work(self) -> str:
        return "Human is working"

    def eat(self) -> str:
        return "Human is eating"


class Robot:
    def work(self) -> str:
        return "Robot is working"
    # No eat() method - and that's fine, Robot never claimed to need it


birds = [FlyingBird(), Penguin()]
for bird in birds:
    print(bird.move())

worker1 = Human()
worker2 = Robot()

print(worker1.work())
print(worker1.eat())
print(worker2.work())
