# lib/models/stores.py
from models.__init__ import CURSOR, CONN


class Store:

    # Dictionary of objects saved to the database.
    all = {}

    # Class constructor method (dunder method)
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
    
    # String representation method (dunder method)
    def __repr__(self):
        return f"<Store {self.id}: {self.name}, {self.category}>"
    
    # Name property 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name[0] + name[1:]
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    # Category property
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category[0] + category[1:]
        else:
            raise ValueError(
                "Category must be a non-empty string"
            )
        
    