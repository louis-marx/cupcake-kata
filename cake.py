"""
Your task is to implement the missing classes and methods to make the tests pass.
Use the Decorator and Composite design patterns.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Cake(ABC):
    """Base interface for all cakes"""

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass


@dataclass
class BaseCake(Cake):
    """Base class for concrete cake types"""
    emoji: str
    base_price: float

    def name(self):
        return self.emoji

    def price(self):
        return self.base_price


@dataclass
class Cupcake(BaseCake):
    """A cupcake implementation"""
    emoji: str = "🧁"
    base_price: float = 1.0


@dataclass
class Cookie(BaseCake):
    """A cookie implementation"""
    emoji: str = "🍪"
    base_price: float = 2.0


@dataclass
class ToppingDecorator(Cake):
    """Base decorator class for cake toppings"""
    cake: Cake
    topping_emoji: str
    topping_price: float

    def name(self):
        base_name = self.cake.name()
        if isinstance(self.cake, ToppingDecorator):
            return f"{base_name} and {self.topping_emoji}"
        else:
            return f"{base_name} with {self.topping_emoji}"

    def price(self):
        return round(self.cake.price() + self.topping_price, 2)


@dataclass
class Chocolate(ToppingDecorator):
    """Chocolate topping decorator"""
    topping_emoji: str = "🍫"
    topping_price: float = 0.1


@dataclass
class Nuts(ToppingDecorator):
    """Nuts topping decorator"""
    topping_emoji: str = "🥜"
    topping_price: float = 0.1


@dataclass
class Sugar(ToppingDecorator):
    """Sugar topping decorator"""
    topping_emoji: str = "🍬"
    topping_price: float = 0.1