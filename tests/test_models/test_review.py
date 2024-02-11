#!/usr/bin/python3
"""Unit Test for The Review Class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review Class"""
    def test_review(self):
        """Test Review"""
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')
