#!/usr/bin/env python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Instantiates a Square with validated size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The computed area of the square.
        """
        return self.__size * self.__size
