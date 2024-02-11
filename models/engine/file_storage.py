#!/usr/bin/python3
"""Module that serializes instances to a JSON file and
deserializes JSON file to instances"""

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
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        dictt = {}
        for key, value in self.__objects.items():
            dictt[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dictt, file)

    def reload(self):
        """deserializes the JSON file to objects"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        instances_dict = {
            'BaseModel': BaseModel, 'Amenity': Amenity,
            'City': City, 'Place': Place, 'Review': Review,
            'State': State, 'User': User
        }
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for value in data.values():
                    self.new(instances_dict[value['__class__']](**value))
        except FileNotFoundError:
            pass
