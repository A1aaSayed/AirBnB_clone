#!/usr/bin/python3
"""Module for State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    name = ''

    def __init__(self, *args, **kwargs):
        """Constractor"""
        super().__init__(*args, **kwargs)
