#!/usr/bin/env python3
"""
Module defining an abstract Shape class and concrete Circle and Rectangle classes.
Also incorporates a standalone shape_info function to demonstrate duck typing.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a specific radius.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int or float: The computed area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int or float: The computed perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape using duck typing.

    Args:
        shape: An object that has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
