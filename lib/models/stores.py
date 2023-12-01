# lib/models/stores.py
from models.__init__ import CURSOR, CONN


class Store:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
