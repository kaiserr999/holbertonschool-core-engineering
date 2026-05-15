#!/usr/bin/env python3
"""
Module providing SwimMixin and FlyMixin.
Also defines a Dragon class demonstrating the use of mixins.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capabilities.
    """

    def swim(self):
        """
        Prints the swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capabilities.
    """

    def fly(self):
        """
        Prints the flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon that uses mixins to fly and swim.
    """

    def roar(self):
        """
        Prints the roaring behavior.
        """
        print("The dragon roars!")
