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


# ==========================================
# 3. MAIN PROGRAM 
# ==========================================
def show_menu():
    print("\n------- MENU -------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------")

# --- Start Program ---
print("=" * 35)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 35)

# Create Inventory object
inventory = Inventory()

while True:
    show_menu()
    option = input("\nEnter option: ").strip()

    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("\nAdd New Product")
        p_id = input("Product ID: ").strip()
        p_name = input("Product Name: ").strip()
        try:
            p_price = float(input("Price: ").strip())
            p_stock = int(input("Stock Quantity: ").strip())
            new_product = Product(p_id, p_name, p_price, p_stock)
            inventory.add_product(new_product)
            print("Product added successfully!")
        except ValueError:
            print("Invalid price or stock quantity. Product not added.")

    elif option == "3":
        print("\nUpdate Stock")
        p_id = input("Enter Product ID: ").strip()
        product = inventory.search_product(p_id)
        if product is not None:
            print("Product Found:")
            print("Name: " + product.get_name())
            print("Current Stock: " + str(product.get_stock()))
            try:
                new_stock = int(input("New Stock Quantity: ").strip())
                product.update_stock(new_stock)
                print("Stock updated successfully!")
            except ValueError:
                print("Invalid stock quantity.")
        else:
            print("Product not found.")

    elif option == "4":
        print("\nSearch Product")
        p_id = input("Enter Product ID: ").strip()
        product = inventory.search_product(p_id)
        if product is not None:
            print("\nProduct Found")
            print("-" * 35)
            print(product.display_information())
            print("-" * 35)
        else:
            print("Product not found.")

    elif option == "5":
        print("Saving not implemented yet.") # Placeholder

    elif option == "6":
        print("Thank you for using Inventory Management System. Program terminated.")
        break