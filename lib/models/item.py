# lib/models/item.py
from models.__init__ import CURSOR, CONN
from models.store import Store

class Store:

    #Dictionary of objects saved to the database
    all = {}

    def __init__(self, name, need, store_id, id=None):
        self.id = id
        self.name = name
        self.need = need
        self.store_id = store_id

    def __repr__(self):
        return f'Item {self.id}: {self.name}, {self.need}, {self.store_id}'
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be non-empty string"
            )
        
    