#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.store import Store
from .models.item import Item
import ipdb

def reset_database():
    Item.drop_table()
    Store.drop_table()
    Item.create_table()
    Store.create_table()


ipdb.set_trace()

reset_database()
