#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""
    
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Properties for the length of a sise of a square.
        
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square.

        Return:
            thee size squared

        """
        return self.__size ** 2
