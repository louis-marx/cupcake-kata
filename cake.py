"""
Your task is to implement the missing classes and methods to make the tests pass.
Use the Decorator and Composite design patterns.
"""

from abc import ABC, abstractmethod


class Cake(ABC):
    """Base interface for all cakes"""

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Cupcake(Cake):
    """A cupcake implementation"""

    def name(self):
        return None

    def price(self):
        return None