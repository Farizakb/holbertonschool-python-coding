#!/usr/bin/python3
"""
Module that defines a Square class with size validation,
area computation, and a print method.
"""


class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the '#' character.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
