#!/usr/bin/python3
"""Module for City Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """Constractor"""
        super().__init__(*args, **kwargs)
