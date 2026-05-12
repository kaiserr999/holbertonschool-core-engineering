#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
            position (tuple, optional): The position of the new square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character.

        If the size is 0, prints an empty line.
        """
        print(self)

    def __str__(self):
        """String representation of the square, handling size and position.

        Returns:
            str: the square formatted to be printed.
        """
        if self.__size == 0:
            return ""

        string_repr = "\n" * self.__position[1]
        for _ in range(self.__size):
            string_repr += " " * self.__position[0] + "#" * self.__size + "\n"

        # Remove trailing newline to avoid adding an extra one when printed
        return string_repr[:-1]
