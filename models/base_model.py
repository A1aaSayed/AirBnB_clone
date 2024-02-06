#!/usr/bin/python3
"""
Module for initialization, serialization and deserialization
 of other instances
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model that defines all common attributes/methods 
    for other classes
    """

    def __init__(self):
        """Initialize instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of instance attributes"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
