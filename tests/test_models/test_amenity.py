#!/usr/bin/python3
"""Unit Test for The Amenity Class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity Class"""
    def test_city(self):
        """Test Amenity"""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')
