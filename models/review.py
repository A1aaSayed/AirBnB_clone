#!/usr/bin/python3
"""Module for State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Constractor"""
        super().__init__(*args, **kwargs)
