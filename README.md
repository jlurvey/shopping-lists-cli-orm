CLI Application for Managing Stores and Items

This Python CLI application provides functionality to manage stores and their associated items using a SQLite database. The application comprises different commands allowing users to create, delete, update, and retrieve information about stores and items. The core functionalities are organized into two main sections: managing stores and managing items.

Usage

To run the application, execute lib/cli.py using Python in your terminal or command prompt.

The user interface displays a menu with options numbered from 0 to 14, each representing a specific action. Users can interact with the application by entering the corresponding number for the desired action.

Commands Available

1.	Create Store: Allows users to create a new store by providing a name and category.
2.	Delete Store: Enables the deletion of a store by entering its ID.
3.	List All Stores: Displays a list of all existing stores.
4.	List Stores by Category: Lists stores filtered by a specific category.
5.	Find Store by Name: Searches for a store by its name.
6.	Find Store by ID: Searches for a store by its unique ID.
7.	Update Store: Modifies an existing store's name or category by providing its ID.
8.	Create Item: Creates a new item associated with a store, requiring a name, need status, and store ID.
9.	Delete Item: Deletes an item by its ID.
10.	List All Items: Displays a list of all items.
11.	List Items by Store: Lists items associated with a particular store, requiring the store's ID.
12.	Find Item by Name: Searches for an item by its name.
13.	Find Item by ID: Searches for an item by its unique ID.
14.	Update Item: Modifies an existing item's details by providing its ID.

Files Overview

lib/cli.py

This file contains the main entry point of the CLI application. It displays a menu and allows users to interact with the functionalities provided by calling various helper functions.

lib/debug.py

This file contains a method reset_database() to reset the database by dropping existing tables and creating new ones. It initializes some sample stores (Publix, TJ, Ace) after resetting the database.

lib/helpers.py

This file holds various helper functions utilized by the CLI application. These functions facilitate the execution of specific commands such as creating, deleting, listing, finding, or updating stores and items.

lib/models/item.py and lib/models/store.py

These files define the models for items and stores, respectively, providing methods to interact with the database. They include functionalities to create tables, perform CRUD operations (Create, Read, Update, Delete), find items or stores by various criteria, and more.

Models Overview

Item Model

The Item model represents items that can be associated with stores. It contains properties for name, need status, and store_id. Users can create, delete, update, or retrieve items using the defined methods.

Store Model

The Store model represents stores with attributes for name and category. Similar to the Item model, users can manage stores by creating, deleting, updating, or retrieving stores using the defined methods.
