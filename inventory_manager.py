# Week 5 Lab: Data Manipulation
import json

def load_inventory():
    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()
        print("inventory.json found. Inventory loaded successfully.")
        return inventory
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
        return []

def save_inventory(inventory):
    file = open("inventory.json", "w")
    json.dump(inventory, file, indent=4)
    file.close()

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    product_name = input("Product Name: ").strip()
    price_input = input("Price: ").strip()
    stock_input = input("Stock Quantity: ").strip()

    if not price_input.replace(".", "").isdigit():
        print("Invalid price.")
        return inventory
    if not stock_input.isdigit():
        print("Invalid stock quantity.")
        return inventory

    price = float(price_input)
    stock = int(stock_input)

    product = {"id": product_id, "name": product_name, "price": price, "stock": stock}
    inventory.append(product)
    print("Product added successfully!")
    return inventory

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print("Name: " + product["name"])
            print("Current Stock: " + str(product["stock"]))
            new_stock = input("\nNew Stock Quantity: ").strip()
            if not new_stock.isdigit():
                print("\nInvalid stock quantity.")
                return inventory
            product["stock"] = int(new_stock)
            print("\nStock updated successfully!")
            return inventory

    print("Product not found.")
    return inventory

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("------------------------------------------------ ")
            print("ID: " + product["id"])
            print("Name: " + product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock: " + str(product["stock"]))
            print("------------------------------------------------ ")
            print()  
            return

    print("Product not found.")

def display_all(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("------------------------------------------------ ")

    for product in inventory:
            print("ID: " + product["id"] + " | Name: " + product["name"] +
                " | Price: $" + format(product["price"], ".2f") + 
                " | Stock: " + str(product["stock"]))
    print("------------------------------------------------ ")

def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

# Main program
print("========================================")
print("# INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()

while True:
    show_menu()
    option = input("\nEnter option: ").strip()

    if option == "1":
        display_all(inventory)
    elif option == "2":
        inventory = add_product(inventory)
    elif option == "3":
        inventory = update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        print("\nSaving Inventory...")
        print("Inventory saved successfully to inventory.json.")
        save_inventory(inventory)
    elif option == "6":
        print("\nSaving inventory before exit...")
        print("Inventory saved successfully.")
        save_inventory(inventory)
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please try again.")