# lib/models/stores.py
from models.__init__ import CURSOR, CONN


class Store:

    # Dictionary of objects saved to the database.
    all = {}

    # Class constructor method (dunder method)
    def __init__(self, name, type, id=None):
        self.id = id
        self.name = name
        self.type = type
    
    # String representation method (dunder method)
    def __repr__(self):
        return f"<Store {self.id}: {self.name}, {type}>"
    
    

