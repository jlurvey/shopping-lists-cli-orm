import sqlite3

CONN = sqlite3.connect('shopping_list.db')
CURSOR = CONN.cursor()
