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

if __name__ == "__main__":
    main()
