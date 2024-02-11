#!/usr/bin/python3
"""Unit Test for The State Class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State Class"""
    def test_state(self):
        """Test State"""
        state = State()
        self.assertEqual(state.name, '')
