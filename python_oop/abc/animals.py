#!/usr/bin/env python3
"""
This module provides an abstract base class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    A class representing a Dog, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound made by a Dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    A class representing a Cat, inheriting from Animal.
    """

    def sound(self):
        """
        Returns the sound made by a Cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
