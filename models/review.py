#!/usr/bin/python3

"""class Review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition"""

    place_id = ""
    user_id = ""
    text = ""
