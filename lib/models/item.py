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