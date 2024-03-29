#!/usr/bin/python3
"""Inherits from baseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class rectangle(BaseGeometry):
    """a class to define rectangke using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
