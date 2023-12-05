# lib/cli.py

from helpers import (
    exit_program,
    create_store,
    delete_store,
    list_stores,
    list_stores_by_category,
    find_store_by_name,
    find_store_by_id,
    update_store,
    create_item,
    delete_item,
    list_items,
    list_items_by_store,
    find_item_by_name,
    find_item_by_id,
    update_item,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")

if __name__ == "__main__":
    main()
