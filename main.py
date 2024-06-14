from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self._age: int = age

    @abstractmethod
    def sound(self) -> str:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not (0 <= value <= 20):
            raise ValueError("Age must be between 0 and 20.")
        self._age = value

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


class SoundMixin:
    def make_sound(self) -> None:
        print(f"{self.name} says {self.sound()}")


class Dog(Animal, SoundMixin):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self._breed: str = breed

    @property
    def breed(self) -> str:
        return self._breed

    @breed.setter
    def breed(self, value: str) -> None:
        if not isinstance(value, str) or not value:
            raise ValueError("Breed must be a non-empty string.")
        self._breed = value

    def sound(self) -> str:
        return "Bark"

    def __repr__(self) -> str:
        return f"({super().__repr__()}, breed={self.breed})"

    def __str__(self) -> str:
        return f"{super().__str__()} and is a {self.breed}"


class Puppy(Dog):
    def __init__(self, name: str, age: int, breed: str, is_vaccinated: bool) -> None:
        super().__init__(name, age, breed)
        self.__is_vaccinated: bool = is_vaccinated

    @property
    def is_vaccinated(self) -> bool:
        return self.__is_vaccinated

    def sound(self) -> str:
        return "Yip"

    def __repr__(self) -> str:
        return f"{super().__repr__()}, is_vaccinated={self.is_vaccinated})"

    def __str__(self) -> str:
        return f"{super().__str__()} and {'is' if self.is_vaccinated else 'is not'} vaccinated."


class Cat(Animal, SoundMixin):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self._color: str = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        if not isinstance(value, str) or not value:
            raise ValueError("Color must be a non-empty string.")
        self._color = value

    def sound(self) -> str:
        return "Meow"

    def __repr__(self) -> str:
        return f"({super().__repr__()}, color={self.color})"

    def __str__(self) -> str:
        return f"{super().__str__()} and is a {self.color} cat."


class Kitten(Cat):
    def __init__(self, name: str, age: float, color: str, is_playful: bool) -> None:
        super().__init__(name, age, color)
        self.__is_playful: bool = is_playful

    @property
    def is_playful(self) -> bool:
        return self.__is_playful

    def sound(self) -> str:
        return "Mew"

    def __repr__(self) -> str:
        return f"{super().__repr__()}, is_playful={self.is_playful})"

    def __str__(self) -> str:
        return f"{super().__str__()} and {'is' if self.is_playful else 'is not'} playful."


class Owner:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._pets: List[Animal] = []

    def add_pet(self, pet: Animal) -> None:
        self._pets.append(pet)

    def __str__(self) -> str:
        pet_list = ', '.join([str(pet) for pet in self._pets])
        return f"{self.name} owns: {pet_list}"


dog: Dog = Dog("Max", 5, "Golden Retriever")
puppy: Puppy = Puppy("Buba", 1, "Labrador", True)
cat: Cat = Cat("Fiko", 3, "black")
kitten: Kitten = Kitten("Fisuka", 0.5, "white", True)

owner: Owner = Owner("Marta")
owner.add_pet(dog)
owner.add_pet(cat)

print(dog)
print(puppy)
print(cat)
print(kitten)
print(owner)
