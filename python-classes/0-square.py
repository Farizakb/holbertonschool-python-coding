#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides the Square class used in the early OOP exercises.
"""


class Square:
    """Represent a square with a private size attribute.

    The size attribute is private to allow future validation and control.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: Initial size of the square (no type/value verification).
        """
        self.__size = size
