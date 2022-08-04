#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
""" Module base_model: class BaseModel """

class BaseModel():
    """
        BaseModel: defines the base model
        Attributes:
            id (string): assigns uuid to an instance
            created_at (datetime): assigns the current date and time the instance is created
            updated_at (datetime): assigns the update time of an instance
        Method:
            __init__ : initializes the instance
            __str__ : prints the instance in a particular format
    """ 
    def __init__(self, id, created_at, updated_at):
        """
            initializes the instance
            Args:
                id (string): assigns uuid to an instance
            created_at (datetime): assigns the current date and time the instanc
e is created
            updated_at (datetime): assigns the update time of an instance
        """
        id = str(uuid4())

