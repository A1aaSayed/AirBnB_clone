#!/usr/bin/python3
"""Unit Test for The City Class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City Class"""
    def test_city(self):
        """Test City"""
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')
