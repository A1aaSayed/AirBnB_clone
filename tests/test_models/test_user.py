#!/usr/bin/python3
"""Unit Test for The User Class"""

import unittest
from models.user import User


class TestCity(unittest.TestCase):
    """Test User Class"""
    def test_user(self):
        """Test User Class"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')
