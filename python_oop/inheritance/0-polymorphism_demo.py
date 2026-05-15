#!/usr/bin/env python3
"""
Tutorial demonstrating inheritance and polymorphism.
"""


class Animal:
    """
    Parent class representing a generic animal.
    """

    def speak(self):
        """
        Defines the generic sound made by an animal.
        """
        return "Some sound"


class Dog(Animal):
    """
    Child class representing a dog.
    """

    def speak(self):
        """
        Defines the sound made by a dog.
        """
        return "Woof"


class Cat(Animal):
    """
    Child class representing a cat.
    """

    def speak(self):
        """
        Defines the sound made by a cat.
        """
        return "Meow"


if __name__ == "__main__":
    # Step 3 and 4: Create Objects and Polymorphism with overridden methods
    dog = Dog()
    cat = Cat()

    print(dog.speak())
    print(cat.speak())

    # Step 5: Demonstrate Polymorphism in a list
    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    # Step 6: Check Class Relationships
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))

    print(issubclass(Dog, Animal))
