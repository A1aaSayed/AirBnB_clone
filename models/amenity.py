#!/usr/bin/python3
"""Module for Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    name = ''

    def __init__(self, *args, **kwargs):
        """Constractor"""
        super().__init__(*args, **kwargs)
