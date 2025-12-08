#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides the Square class used in the early OOP exercises.
"""

class Square(object):
    """Represent a square with a private size attribute.

    The size attribute is private to allow the class author to control
    access and validation in later tasks.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: initial size of the square (no type/value verification).
        """
        self.__size = size
