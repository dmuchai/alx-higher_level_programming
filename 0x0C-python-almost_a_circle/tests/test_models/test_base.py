#!/usr/bin/python3
""" Module for testing Base class functionality """

import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBaseClass(unittest.TestCase):
    """ Test suite for the Base class """

    def setUp(self):
        """ Method executed before each test """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """ Test manually assigned id """
        instance = Base(1)
        self.assertEqual(instance.id, 1)

    def test_default_id(self):
        """ Test default id assignment when none is provided """
        instance = Base()
        self.assertEqual(instance.id, 1)

    def test_multiple_ids(self):
        """ Test ids assigned across multiple instances """
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)

    def test_combined_ids(self):
        """ Test a mix of automatic and manually assigned ids """
        instance1 = Base()
        instance2 = Base(1024)
        instance3 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 1024)
        self.assertEqual(instance3.id, 2)

    def test_string_id(self):
        """ Test id as a string """
        instance = Base('1')
        self.assertEqual(instance.id, '1')

    def test_excess_arguments(self):
        """ Test initializing with too many arguments """
        with self.assertRaises(TypeError):
            instance = Base(1, 1)

    def test_private_attribute_access(self):
        """ Test that private attributes cannot be accessed """
        instance = Base()
        with self.assertRaises(AttributeError):
            instance.__nb_objects

    def test_to_json_string_none(self):
        """ Test converting None to JSON string """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """ Test converting an empty list to JSON string """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """ Test converting a valid list of dictionaries to JSON string """
        dict_list = [{'id': 12}]
        self.assertEqual(Base.to_json_string(dict_list), '[{"id": 12}]')

    # Tests for from_json_string
    def test_from_json_string_none(self):
        """ Test converting None from JSON string """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """ Test converting an empty JSON string """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """ Test converting a valid JSON string to list of dictionaries """
        json_str = '[{"id": 89}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 89}])

    def test_save_to_file_with_none(self):
        """ Test saving None to a JSON file """
        Square.save_to_file(None)
        expected_result = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), expected_result)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_for_rectangle(self):
        """ Test saving a Rectangle instance to a JSON file """
        Rectangle.save_to_file(None)
        expected_result = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), expected_result)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
