#!/usr/bin/python3
"""
Contains definition of class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of class Rectangle that inherits from BaeGeometry
        Attributes:
            width (int): width of the Rectangle.
            height (int) height of the Rectangle.
    """

    def __init__(self, width, height):
        """Initializing an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
