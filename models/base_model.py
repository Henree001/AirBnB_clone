#!/usr/bin/python3
""" Class Base Model """
import uuid
from datetime import datetime
import models


class BaseModel:
    """A baseclass for future subclasses """
    def __init__(self, *args, **kwargs):
        """ Instantiates the base model variables"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(v)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ create a string that prints class name, id, dict """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates the updated_at variable with the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary of the instance attributes"""
        newdict = self.__dict__.copy()
        newdict['created_at'] = newdict['created_at'].isoformat()
        newdict["updated_at"] = newdict["updated_at"].isoformat()
        newdict['__class__'] = self.__class__.__name__
        return newdict
