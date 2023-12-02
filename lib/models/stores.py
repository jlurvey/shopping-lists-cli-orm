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
            self._name = name[0].upper() + name[1:].lower()
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
            self._category = category[0].upper() + category[1:].lower()
        else:
            raise ValueError(
                "Category must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Store instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Store instances"""
        sql = """
            DROP TABLE IF EXISTS stores;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name and category values of the current Store instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO departments (name, category)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.category))
        CONN.commit()        