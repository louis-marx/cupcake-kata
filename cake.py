"""
Your task is to implement the missing classes and methods to make the tests pass.
Use the Decorator and Composite design patterns.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

TOPPING_PRICE = 0.1
BUNDLE_DISCOUNT = 0.9


class Cake(ABC):
    """Base interface for all cakes"""

    @abstractmethod
    def name(self):
        return None

    @abstractmethod
    def price(self):
        return None


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
    topping_price: float = TOPPING_PRICE

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


@dataclass
class Nuts(ToppingDecorator):
    """Nuts topping decorator"""
    topping_emoji: str = "🥜"


@dataclass
class Sugar(ToppingDecorator):
    """Sugar topping decorator"""
    topping_emoji: str = "🍬"


@dataclass
class Bundle(Cake):
    """Bundle of cakes with discount"""
    cakes: list[Cake]

    def name(self):
        if len(self.cakes) == 1:
            return self.cakes[0].name()
        return "\n".join(cake.name() for cake in self.cakes)

    def price(self):
        total_price = 0
        for cake in self.cakes:
            if isinstance(cake, Bundle):
                total_price += sum(nested_cake.price() for nested_cake in cake.cakes)
            else:
                total_price += cake.price()
        return round(total_price * BUNDLE_DISCOUNT, 2)