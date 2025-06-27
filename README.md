# Inventory-Management-System
A fully functional Inventory Management System developed in Python using Object-Oriented Programming, file handling, and a command-line interface. It allows users to add, update, delete, and search inventory items, generate reports, and check low stock levels. Ideal for small-scale stores and educational projects.
# 🛒 Inventory Management System (Python CLI)

This project is a complete Inventory Management System built with Python. It uses Object-Oriented Programming (OOP) principles and file handling to manage product records. The system runs in the command-line interface and provides a secure login and full inventory management functionality.

## 🔧 Features

- Add new items to inventory
- Update existing item details
- Delete items by ID
- Search items by name
- Generate a full inventory report
- Check for items with low stock
- Persistent data storage in `invent.txt`
- Security code required to access the system

## Project Structure
item.py # Defines the Item class and properties
Inventory.py # Contains inventory management logic
main.py # User interface and menu loop
invent.txt # File used for data storage
README.md # Project documentation

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arsal1947/Python-Inventory-Management.git
   cd Python-Inventory-Management
Run the program:

python main.py
Enter the access code when prompted:

PLEASE! ENTER CODE: 1122
Item Attributes
ID: Unique integer identifier

Name: Item name

Category: Type or classification of item

Quantity: Current stock level (non-negative integer)

Price: Cost of the item (non-negative float)

Technologies Used
Python 3

OOP (Object-Oriented Programming)

File Handling (.txt file for saving data)
