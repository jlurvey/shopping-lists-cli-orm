# lib/models/item.py
from models.__init__ import CURSOR, CONN
from models.store import Store

class Item:

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
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name[0].upper() + name[1:].lower()
        else:
            raise ValueError("Name must be non-empty string")
        
    @property
    def need(self):
        return self._need

    @need.setter
    def need(self, need):
        if isinstance(need, bool):
            self._need = need
        else:
            raise ValueError("Need must be boolean value")
        
    @property
    def store_id(self):
        return self._store_id
    
    @store_id.setter
    def store_id(self, store_id):
        if isinstance(store_id, int) and Store.find_by_id(store_id):
            self._store_id = store_id
        else:
            raise ValueError("store_id must reference a store in the database")
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Item instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            need BOOLEAN,
            store_id INTEGER,
            FOREIGN KEY (store_id) REFERENCES stores(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Item instances"""
        sql = """
            DROP TABLE IF EXISTS items
        """
        CURSOR.execture(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, need, and store id values of the current Item object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's primary key as dictionary key"""
        sql = """
            INSERT INTO items (name, need, store_id)
            VALUES = (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.need, self.store_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Item object."""
        sql = """
            UPDATE items
            SET name = ?, need = ?, store_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.need, self.store_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Item object"""
        sql = """
            DELETE FROM items
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, need, store_id):
        """Initialize a new Item instance and save the object to the database"""
        item = cls(name, need, store_id)
        item.save()
        return item
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Item object having the attribute values from the table row"""
        item = cls.all.get(row[0])
        if item:
            item.name = row[1]
            item.need = row[2]
            item.store_id = row[3]
        else:
            item = cls(row[1], row[2], row[3])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Item object per table row"""
        sql = """
            SELECT *
            FROM items
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Item object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM items
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        return [cls.instance_from_db(row) if row else None]
    
    @classmethod
    def find_by_name(cls, name):
        """Return Item object corresponding to the table row matching the specified name"""
        sql = """
            SELECT *
            FROM items
            WHERE NAME = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        return[cls.instance_from_db(row) if row else None]
