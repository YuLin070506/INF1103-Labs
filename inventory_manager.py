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


