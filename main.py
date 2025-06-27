from item import Item
from Inventory import InventoryManagementSystem

def displayMenu():
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Search Item by Name")
    print("5. Generate Report")
    print("6. Check Low Stock")
    print("7. Exit")

ims = InventoryManagementSystem()

# Login security (optional)
code = input("PLEASE! ENTER CODE: ")
while code != "1122":
    code = input("INVALID CODE! ENTER AGAIN: ")

while True:
    displayMenu()
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            id_ = int(input("Enter Item ID: "))
            name = input("Enter Item Name: ")
            category = input("Enter Category: ")
            quantity = int(input("Enter Quantity: "))
            while quantity < 0:
                quantity = int(input("Quantity cannot be negative. Enter again: "))
            price = float(input("Enter Price: "))
            while price < 0:
                price = float(input("Price cannot be negative. Enter again: "))

            new_item = Item(name, category, id_, quantity, price)
            ims.addItem(new_item)
        except ValueError:
            print("Invalid input. Please enter correct values.")

    elif choice == "2":
        try:
            id_ = int(input("Enter Item ID to update: "))
            name = input("Enter New Name: ")
            category = input("Enter New Category: ")
            quantity = int(input("Enter New Quantity: "))
            while quantity < 0:
                quantity = int(input("Quantity cannot be negative. Enter again: "))
            price = float(input("Enter New Price: "))
            while price < 0:
                price = float(input("Price cannot be negative. Enter again: "))

            updated_item = Item(name, category, id_, quantity, price)
            ims.updateItem(id_, updated_item)
        except ValueError:
            print("Invalid input.")

    elif choice == "3":
        try:
            id_ = int(input("Enter Item ID to delete: "))
            ims.deleteItem(id_)
        except ValueError:
            print("Invalid ID.")

    elif choice == "4":
        name = input("Enter Item Name to search: ")
        ims.searchByName(name)

    elif choice == "5":
        ims.generateReport()

    elif choice == "6":
        try:
            threshold = int(input("Enter stock threshold: "))
            ims.checkLowStock(threshold)
        except ValueError:
            print("Invalid quantity.")

    elif choice == "7":
        print("Exiting... Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")

