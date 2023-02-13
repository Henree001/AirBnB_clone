#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
