#!/usr/bin/python3
"""
Module that serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json


class FileStorage:
    """File Storage Class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Method that returns the dictionary objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in objects the obj with key"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        serialized_dict = {}
        for key, value in self.__objects.items():
            serialized_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_dict, file)
    
    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    name, id_ = key.split('.')
                    class_ = eval(name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
