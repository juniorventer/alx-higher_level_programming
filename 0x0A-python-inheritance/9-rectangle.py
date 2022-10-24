#!/usr/bin/python3
"""
Contains definition of class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of class Rectangle that inherits from BaseGeometry.
        Attributes:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.
    """

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        
        self.__height = heigh

    def area(self):
        """Returns are of the Rectangle"""
        
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Returns string representation of an instance of class Rectangle
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                    self.__width,self.__height)
