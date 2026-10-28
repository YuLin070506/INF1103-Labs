import json

# ==========================================
# 1. PRODUCT CLASS 
# ==========================================
class Product:
    def __init__(self, product_id, name, price, stock):
        # private attributes 
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def update_stock(self, new_quantity):
        self.__stock = int(new_quantity)

    def display_information(self):
        return f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}"

    # Getters
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    # helper method 
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


# ==========================================
# 2. INVENTORY CLASS 
# ==========================================
class Inventory:
    def __init__(self):
        # private list to store Product objects
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None # return None if not found

    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        print("-" * 35)
        for product in self.__products:
            print(product.display_information())
        print("-" * 35)

    def get_all_products(self):
        return self.__products
