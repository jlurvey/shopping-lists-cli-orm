#!/usr/bin/env python3
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
        elif choice == "1":
            create_store()
        elif choice == "2":
            delete_store()
        elif choice == "3":
            list_stores()
        elif choice == "4":
            list_stores_by_category()
        elif choice == "5":
            find_store_by_name()
        elif choice == "6":
            find_store_by_id()
        elif choice == "7":
            update_store()
        elif choice == "8":
            create_item()
        elif choice == "9":
            delete_item()
        elif choice == "10":
            list_items()
        elif choice == "11":
            list_items_by_store()
        elif choice == "12":
            find_item_by_name()
        elif choice == "13":
            find_item_by_id()
        elif choice == "14":
            update_item()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create store")
    print("2. Delete store")
    print("3. List all stores")
    print("4. List stores by category")
    print("5. Find store by name")
    print("6. Find store by id")
    print("7. Update store")
    print("8. Create item")
    print("9. Delete item")
    print("10. List all items")
    print("11. List items by store")
    print("12. Find item by name")
    print("13. Find item by id")
    print("14. Update item")


if __name__ == "__main__":
    main()
