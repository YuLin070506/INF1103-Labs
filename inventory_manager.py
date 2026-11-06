import json
from abc import ABC, abstractmethod

# ==========================================
# 1. INTERFACES CLASS 
# ==========================================
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# ==========================================
# 2. PRODUCT CLASS 
# ==========================================
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
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

    @abstractmethod
    def get_fullment_info(self):
        pass

# ==========================================
# 3. SUBCLASSES 
# ==========================================
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def display_information(self):
        # Reuse parent method, add weight (Lab 2.1)
        base_info = super().display_information()
        return f"{base_info} | Weight: {self.__weight} kg"

    def get_fullment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.00

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def display_information(self):
        # Reuse parent method, add download size (Lab 2.1)
        base_info = super().display_information()
        return f"{base_info} | Download Size: {self.__download_size} MB"

    def get_fullment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

# ==========================================
# 4. INVENTORY CLASS
# ==========================================
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

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
# 5. MAIN PROGRAM
# ==========================================
def load_inventory():
    inventory = Inventory()
    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()
        
        # Check the type identifier to instantiate the correct class
        for item in data:
            if item.get("type") == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
            elif item.get("type") == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])
            else:
                # Fallback for older data just in case
                continue 
            inventory.add_product(product)
            
        print("inventory.json found. Inventory loaded successfully.")
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
    
    return inventory

def save_inventory(inventory):
    file = open("inventory.json", "w")
    data_to_save = []
    for product in inventory.get_all_products():
        data_to_save.append(product.to_dict())
        
    json.dump(data_to_save, file, indent=4)
    file.close()
    print("Inventory saved successfully to inventory.json.")

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
if __name__ == "__main__":
    # --- Start Program ---
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 35)

    inventory = load_inventory() 

    while True:
        show_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("\nAdd New Product")
            p_id = input("Product ID: ").strip()
            p_name = input("Product Name: ").strip()
            
            print("Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")
            p_type = input("Select type (1 or 2): ").strip()

            try:
                p_price = float(input("Price: ").strip())
                p_stock = int(input("Stock Quantity: ").strip())
                
                if p_type == "1":
                    p_weight = float(input("Weight (kg): ").strip())
                    new_product = PhysicalProduct(p_id, p_name, p_price, p_stock, p_weight)
                elif p_type == "2":
                    p_size = float(input("Download Size (MB): ").strip())
                    new_product = DigitalProduct(p_id, p_name, p_price, p_stock, p_size)
                else:
                    print("Invalid product type. Product not added.")
                    continue # skip to next loop iteration

                inventory.add_product(new_product)
                print("Product added successfully!")
            except ValueError:
                print("Invalid numeric input. Product not added.")

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
            save_inventory(inventory)

        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System. Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")