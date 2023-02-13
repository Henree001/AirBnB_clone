#!/usr/bin/python3
""" UnitTest for filestorage """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Tests the file storage """
    def setUp(self):
        """
            Sets up an instance of storage and refreshes the __object to {}
            reload in our case will create a file with an empty dictionary
        """
        self.storage = FileStorage()
        self.storage._refresh()
        self.storage.reload()

    def test_theirs(self):
        """ Test their testcase """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        test_dict = my_model.to_dict()
        new_model = BaseModel(**test_dict)
        self.assertEqual(new_model.id, my_model.id)

    def test_all(self):
        """ Tests if all returns a dictionary """
        dic = self.storage.all()
        self.assertEqual(type(dic), dict)

    def test_all_value(self):
        """ Tests the return value of al() """
        self.assertEqual(self.storage.all(), {})

    """ Save: Saves the dictionary stored in __object to a file """
    def test_save_empty(self):
        """ Tests if save wrote to the file an empty dictionary """
        self.storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            self.r = f.read()
            self.assertEqual(self.r, "{}")

    def test_save(self):
        base = BaseModel()
        pre_obj = self.storage.all()
        self.storage.save()
        after_obj = self.storage.all()
        self.assertEqual(pre_obj, after_obj)

    """ new: stores inside of __object a dictionary rep of the given object """
    def test_new(self):
        """ tests if storage was incremented by one object """
        self.base = BaseModel()
        self.base.id = '121212'
        self.storage.new(self.base)
        test_dic = self.storage.all()
        self.assertTrue(test_dic['BaseModel.121212'])

    @unittest.expectedFailure
    def test_new_if_classes_of_basemodel(self):
        """ Tests new by providing a bad object """
        self.storage.new([])

    """ reload: returns a dictionary stored inside of a file """
    def test_reload(self):
        """ test if reload properly loads the dictionary object with 2 items"""
        self.test_dictionary = {"BaseModel.121212": {"id": 121212}}
        self.test_dictionary["BaseModel.221212"] = {"id": 121212}
        with open("file.json", 'w+') as f:
            json.dump(self.test_dictionary, f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)

    def test_reload_no_existing_file(self):
        """ Tests reload with no existing file """
        if os.path.isfile('file.json'):
            os.remove('file.json')
        self.storage.reload()
        self.assertFalse(os.path.isfile('file.json'))

    def test_private_file(self):
        """ Test that private variables exist """
        with self.assertRaises(AttributeError):
            FileStorage.__file_path

    def test_private_object(self):
        """ Test that private variables exist """
        with self.assertRaises(AttributeError):
            FileStorage.__objects
