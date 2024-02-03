# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod


class AbstractPhysicalObject(ABC):
    def __init__(self, material: str, weight: float) -> None:
        self.material = material
        self.weight = weight

    @abstractmethod
    def move(self, new_location: str) -> None:
        pass

    @abstractmethod
    def break_into_pieces(self) -> None:
        pass


class AbstractLivingBeing(ABC):
    def __init__(self, species: str, habitat: str) -> None:
        self.species = species
        self.habitat = habitat

    @abstractmethod
    def eat(self, food: str) -> None:
        pass

    @abstractmethod
    def reproduce(self) -> None:
        pass


class AbstractConcept(ABC):

    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category

    @abstractmethod
    def manipulate(self, action: str) -> None:
        pass

    @abstractmethod
    def analyze(self) -> str:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
