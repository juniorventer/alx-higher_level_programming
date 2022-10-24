#!/usr/bin/python3
"""
10-rectangle.py
a class Rectangle that inherits from Rectangle (9-rectangle.py)
add calculate are and size
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and validate with interger validator"""

    def __init__(self, size):
        """Validate size of integer rectangle area"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
        """super is used to modify in the parent class"""
