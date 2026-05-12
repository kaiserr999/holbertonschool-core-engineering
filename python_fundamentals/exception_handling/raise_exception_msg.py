#!/usr/bin/env python3
"""Module to raise a NameError with a custom message."""


def raise_exception_msg(message=""):
    """Raises a NameError with the provided message.
    
    Args:
        message: Custom message for the NameError
        
    Raises:
        NameError: With the provided message
    """
    raise NameError(message)
