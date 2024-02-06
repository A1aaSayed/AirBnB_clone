#!/usr/bin/python3
"""Unit Test for The Base Model"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_init(self):
        """Test init method"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        """Test str method"""
        model = BaseModel()
        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        current_updated_at = model.updated_at
        self.assertNotEqual(previous_updated_at, current_updated_at)

    def test_to_dict(self):
        """Test dict Method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
