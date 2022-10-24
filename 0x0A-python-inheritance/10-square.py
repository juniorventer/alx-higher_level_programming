#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Method of initializing a square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method that returns area of square"""
        return self.__size ** 2
