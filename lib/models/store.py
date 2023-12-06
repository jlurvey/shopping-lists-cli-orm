# lib/models/store.py
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

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, category):
        """Initialize a new Store instance and save the object to the database"""
        store = cls(name, category)
        store.save()
        return store

    def update(self):
        """Update the table row corresponding to the current Store instance."""
        sql = """
            UPDATE stores
            SET name = ?, category = ?
            WHERE id = /
        """

        CURSOR.execute(sql, (self.name, self.category, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Store instance,
        delete the dicitonary entry and reassiogn id attribute"""

        sql = """
            DELETE FROM stores
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        # Delete dicitionary and set id to none
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return Store object having the attribute values from the table row."""

        # Check dictionary for an existing instance using the row's primary key
        store = cls.all.get(row[0])
        if store:
            # ensure attributes match row values in case local instance was modified
            store.name = row[1]
            store.category = row[2]
        else:
            # not in dictionary, create new instance and add
            store = cls(row[1], row[2])
            store.id = row [0]
            cls.all[store.id] = store
        return store
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Store object per row in the table"""
        sql = """
            SELECT *
            FROM stores
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Store object corresponding to table row matching id"""
        sql = """
            SELECT *
            FROM stores
            WHERE id =?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Store object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM stores
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def items(self):
        """Return list of items associated with current store"""
        from models.item import Item
        sql = """
            SELECT * FROM items
            WHERE store_id = ?
        """
        CURSOR.execute(sql, (self.id),)

        rows =CURSOR.fetchall()
        return [Item.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_category(cls, category):
        """Return Store objects corresponding to table rows matching the specified category"""
        sql = """
            SELECT *
            FROM stores
            WHERE category = ?
        """

        rows = CURSOR.execute(sql, (category,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
