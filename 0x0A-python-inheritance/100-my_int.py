#!/usr/bin/python3

"""this ,pdule defines a class MyInt that inherits from int"""

clas MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):

        """Override == operator with != behavior"""
            return self.real != value


    def __ne_-(self, value):
        """Override != operator with == behaviour"""
            return self.real == value
