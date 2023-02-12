#!/usr/bin/python3
""" Class Filestorage"""
import json


class FileStorage:
    """Representing a class Filestorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        string = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[string] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {}
        for k, v in self.__objects.items():
            obj_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                json_dict = json.load(f)
            for k, v in json_dict.items():
                class_name = k.split('.')
                self.__objects[k] = eval('{} (**{})'.format(class_name[0], v))
        except Exception:
            pass
