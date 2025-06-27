class Item:
    def __init__(self, name, category, id_, quantity, price):
        self.name = name
        self.category = category
        self.id_ = id_
        self.quantity = quantity
        self.price = price

    def displayItem(self):
        print(f"ID: {self.id_}\n"
              f"Name: {self.name}\n"
              f"Category: {self.category}\n"
              f"Quantity: {self.quantity}\n"
              f"Price: {self.price}")

    # we can also use this dundar or magic method
    # def __str__(self):
    # return f"{self.id_}, {self.name}, {self.category}, {self.quantity}, {self.price}"
    #there is no need of getters and setters because we also access them by using a.name = "Lays" , print(a.name)

    @property
    def getName(self):
        return self.name

    @getName.setter
    def getName(self, name):
        self.name = name

    @property
    def getCategory(self):
        return self.category

    @getCategory.setter
    def getCategory(self, category):
        self.category = category

    @property
    def getId(self):
        return self.id_

    @getId.setter
    def getId(self, id_):
        self.id_ = id_

    @property
    def getQuantity(self):
        return self.quantity

    @getQuantity.setter
    def getQuantity(self, quantity):
        self.quantity = quantity

    @property
    def getPrice(self):
        return self.price

    @getPrice.setter
    def getPrice(self, price):
        self.price = price
