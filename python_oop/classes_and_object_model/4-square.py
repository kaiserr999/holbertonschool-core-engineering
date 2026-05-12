#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
        """
        self.size = size  # This calls the setter property automatically

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
