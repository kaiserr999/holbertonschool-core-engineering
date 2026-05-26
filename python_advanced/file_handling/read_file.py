#!/usr/bin/env python3
"""
Module for reading and printing a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
