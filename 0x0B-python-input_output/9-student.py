#!/usr/bin/python3
"""This module defines a class student"""

class Student:
    """Representr a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to json(self):
        """Gets a dictionary representation"""
        return self.__dict__
