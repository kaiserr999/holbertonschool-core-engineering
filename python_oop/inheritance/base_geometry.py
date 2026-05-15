#!/usr/bin/env python3
"""
This module defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    A base geometry class that provides shared functionality.
    """

    def area(self):
        """
        Computes the area of a geometric shape.

        Raises:
            Exception: indicating that the area calculation
            is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a valid positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
