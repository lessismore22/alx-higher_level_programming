#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    creating test cases for the base module
'''

class TestBase(unittest.TestCase):
    '''
    Testing base
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''

        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id
        '''

        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Sending a negative id
        '''

        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            Sending an id that is not an int
        '''

        b = Base("Betty")
        self.assertEqual("Betty", b.id)

        def test_id_dict(self):
            '''
                Sending an id that is not an int
            '''
            b = Base({"id": 109})
            self.assertEqual({"id": 109}, b.id)

        def test_id_tuple(self):
            '''
                Sending an id that is not an int
            '''
            b = Base((8, ))
            self.assertEqual((8, ), b.id)

        def test_to_json_type(self):
            '''
                Testing the json string
            '''
            sq = Square(1, 0, 0, 609)

            json_dict = sq.to_dictionary()

            json_string = Base.to._json_string(None)

            self.assertEqual(json_string, "[]")

    class TestSquare(unittest.TestCase):
        """
        class for testing class' methods

        """

        @classmethod
        def setUpClass(cls):
            """
                Set up class method for the doc tests
            """

            cls.setup = inspect.getmembers(Base, inspect.isfunction)
        def test_module_docstring(self):
            """
                Tests if module docstring documentation exist
            """
            self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
