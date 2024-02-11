#!/usr/bin/python3
"""Module for User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Constractor"""
        super().__init__(*args, **kwargs)
