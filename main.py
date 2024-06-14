from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @abstractmethod
    def sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 20):
            raise ValueError("Age must be between 0 and 20.")
        self._age = value

    def __repr__(self):
        return f"Animal(name={self.name}, age={self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class SoundMixin:
    def make_sound(self):
        print(f"{self.name} says {self.sound()}")


class Dog(Animal, SoundMixin):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Breed must be a non-empty string.")
        self._breed = value

    def sound(self):
        return "Bark"

    def __repr__(self):
        return f"({super().__repr__()}, breed={self.breed})"

    def __str__(self):
        return f"{super().__str__()} and is a {self.breed}"


class Puppy(Dog):
    def __init__(self, name, age, breed, is_vaccinated):
        super().__init__(name, age, breed)
        self.__is_vaccinated = is_vaccinated

    @property
    def is_vaccinated(self):
        return self.__is_vaccinated

    def sound(self):
        return "Yip"

    def __repr__(self):
        return f"{super().__repr__()}, is_vaccinated={self.is_vaccinated})"

    def __str__(self):
        return super().__str__()


class Cat(Animal, SoundMixin):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Color must be a non-empty string.")
        self._color = value

    def sound(self):
        return "Meow"

    def __repr__(self):
        return f"({super().__repr__()}, color={self.color})"

    def __str__(self):
        return f"{super().__str__()} and is {self.color} cat."


class Kitten(Cat):
    def __init__(self, name, age, color, is_playful):
        super().__init__(name, age, color)
        self.__is_playful = is_playful

    @property
    def is_playful(self):
        return self.__is_playful

    def sound(self):
        return "Mew"

    def __repr__(self):
        return f"{super().__repr__()}, is_playful={self.is_playful})"

    def __str__(self):
        return f"{super().__str__()} and {'is' if self.is_playful else 'is not'} playful."


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Animal):
            raise ValueError("Please provide an animal")
        self._pets.append(pet)

    def __str__(self):
        pet_list = ', '.join([str(pet) for pet in self._pets])
        return f"{self.name} owns: {pet_list}"


dog = Dog("Max", 5, "Golden Retriever")
puppy = Puppy("Buba", 1, "Labrador", True)
cat = Cat("Fiko", 3, "black")
kitten = Kitten("Fisuka", 0.5, "white", True)

owner = Owner("Gvantsa")
owner.add_pet(dog)
owner.add_pet(cat)

print(dog)
print(puppy)
print(cat)
print(kitten)
print(owner)
