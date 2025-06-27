import os
from item import Item

filename = "invent.txt"

class InventoryManagementSystem:
    
    def __init__(self):
        self.inventory = []
        self.itemCount = 0
        self.loadFromFile()

    def saveToFile(self):
        if not os.path.exists(filename):
            open(filename, "w").close()

        with open(filename, "w") as f:
            for item in self.inventory:
                f.write(f"ID: {item.getId}, "
                        f"Name: {item.getName}, "
                        f"Category: {item.getCategory}, "
                        f"Quantity: {item.getQuantity}, "
                        f"Price: {item.getPrice}\n")
        print("Inventory saved to file successfully.")

    def loadFromFile(self):
        try:
            with open(filename, "r") as f:
                self.inventory = []
                for line in f:
                    if line.strip():
                        parts = line.replace("ID: ", "").replace("Name: ", "").replace("Category: ", "") \
                                    .replace("Quantity: ", "").replace("Price: ", "").strip().split(", ")
                        if len(parts) == 5:
                            id_ = int(parts[0])
                            name = parts[1]
                            category = parts[2]
                            quantity = int(parts[3])
                            price = float(parts[4])
                            item = Item(name, category, id_, quantity, price)
                            self.inventory.append(item)
                self.itemCount = len(self.inventory)
                print("Inventory loaded successfully from file.")
        except FileNotFoundError:
            print("No file found.")

    def addItem(self, item):
        for existing_item in self.inventory:
            if existing_item.getId == item.getId:
                print(f"The product with ID {item.getId} is already present.")
                return
        self.inventory.append(item)
        self.itemCount += 1
        self.saveToFile()
        print("Item added successfully.")

    def updateItem(self, id_, updated_item):
        for i in range(len(self.inventory)):
            if self.inventory[i].getId == id_:
                self.inventory[i] = updated_item
                self.saveToFile()
                print("Item updated successfully.")
                return
        print(f"Item with ID {id_} is not present.")

    def deleteItem(self, id_):
        for i in range(len(self.inventory)):
            if self.inventory[i].getId == id_:
                del self.inventory[i]
                self.itemCount -= 1
                self.saveToFile()
                print(f"Item with ID {id_} deleted successfully.")
                return
        print(f"Item with ID {id_} not found.")

    def generateReport(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\n--- Inventory Report ---")
            for item in self.inventory:
                item.displayItem()
                print("------------------------")

    def searchByName(self, name):
        found = False
        for item in self.inventory:
            if item.getName.lower() == name.lower():
                item.displayItem()
                found = True
        if not found:
            print(f"No item found with name '{name}'.")

    def checkLowStock(self, threshold):
        found = False
        print("\n--- Low Stock Items ---")
        for item in self.inventory:
            if item.getQuantity <= threshold:
                item.displayItem()
                found = True
        if not found:
            print("No items found with low stock.")
