#!/usr/bin/python3
"""Unit Test for The File Storage Model"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up method to initialize FileStorage"""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method"""

    def test_new(self):
        """Test the new method"""

    def test_save(self):
        """Test the save method"""

    def test_reload(self):
        """Test the reload method"""

if __name__ == '__main__':
    unittest.main()
