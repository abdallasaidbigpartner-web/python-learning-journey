"""
Lesson 15: SOLID Principles (Single Responsibility + Open/Closed)

Demonstrates separating unrelated responsibilities into distinct
classes (Single Responsibility), and designing for extension without
modifying existing code via a strategy pattern (Open/Closed).
"""

from typing import Protocol


class DiscountStrategy(Protocol):
    """Interface for any discount calculation strategy."""
    def apply(self, price: float) -> float:
        ...


class NoDiscount:
    def apply(self, price: float) -> float:
        return price


class TenPercentOff:
    def apply(self, price: float) -> float:
        return price * 0.9


class Order:
    """Handles only order calculation logic - single responsibility."""

    def __init__(self, price: float, discount: DiscountStrategy):
        self.price = price
        self.discount = discount

    def calculate_total(self) -> float:
        return self.discount.apply(self.price)


class OrderRepository:
    """Handles only saving orders - separate responsibility."""

    def save(self, order: Order) -> None:
        print(f"Order saved with total: {order.calculate_total()}")


order1 = Order(100, NoDiscount())
order2 = Order(100, TenPercentOff())

repo = OrderRepository()
repo.save(order1)
repo.save(order2)
