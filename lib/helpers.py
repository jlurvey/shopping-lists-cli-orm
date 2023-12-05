# lib/helpers.py
from models.store import Store
from models.item import Item


def exit_program():
    print("Goodbye!")
    exit()


def create_store():
    name = input("Enter the store's name: ")
    category = input("Enter the store's category: ")
    try:
        store = Store.create(name, category)
        print(f'Success: {store}')
    except Exception as exc:
        print("Error creating store: ", exc)


def delete_store():
    id_ = input("Enter the store's id: ")
    if store := Store.find_by_id(id_):
        store.delete()
        print(f'Store {id_} deleted')
    else:
        print(f'Store {id_} not found')
        

def list_stores():
    stores = Store.get_all()
    for store in stores:
        print(store)


def list_stores_by_category():
    pass


def find_store_by_name():
    name = input("Enter the store's name: ")
    store = Store.find_by_name(name)
    print(store) if store else print(f'Store {name} not found')


def find_store_by_id():
    id_ = input("Enter the store's id: ")
    store = Store.find_by_id(id_)
    print(store) if store else print(f'Store {id_} not found')

