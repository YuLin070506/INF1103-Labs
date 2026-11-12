import json
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory
from order import Order

def load_inventory() -> Inventory:
    inventory = Inventory()
    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()
        
        for item in data:
            # Reconstruct Supplier
            supplier = Supplier(item.get("supplier_id", "UNKNOWN"), item.get("supplier_name", "Unknown"), item.get("supplier_email", "N/A"))
            
            if item.get("type") == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["weight"])
            elif item.get("type") == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["download_size"])
            else:
                continue 
            inventory.add_product(product)
            
        print("inventory.json found. Inventory loaded successfully.")
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
    
    return inventory

def save_inventory(inventory: Inventory) -> None:
    file = open("inventory.json", "w")
    data_to_save = []
    for product in inventory.products:
        data_to_save.append(product.to_dict())
        
    json.dump(data_to_save, file, indent=4)
    file.close()
    print("Inventory saved successfully to inventory.json.")

def show_menu() -> None:
    print("\n------- MENU -------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Create an Order (Composition)")
    print("6. Save Inventory")
    print("7. Exit")
    print("--------------------")

if __name__ == "__main__":
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
            
            print("Product Type:\n1. Physical\n2. Digital")
            p_type = input("Select type (1 or 2): ").strip()

            print("\n--- Supplier Info ---")
            s_id = input("Supplier ID: ").strip()
            s_name = input("Supplier Name: ").strip()
            s_email = input("Supplier Email: ").strip()
            supplier = Supplier(s_id, s_name, s_email)

            try:
                p_price = float(input("Price: ").strip())
                p_stock = int(input("Stock Quantity: ").strip())
                
                if p_type == "1":
                    p_weight = float(input("Weight (kg): ").strip())
                    new_product = PhysicalProduct(p_id, p_name, p_price, p_stock, supplier, p_weight)
                elif p_type == "2":
                    p_size = float(input("Download Size (MB): ").strip())
                    new_product = DigitalProduct(p_id, p_name, p_price, p_stock, supplier, p_size)
                else:
                    print("Invalid product type.")
                    continue

                inventory.add_product(new_product)
                print("Product added successfully!")
            except ValueError:
                print("Invalid numeric input. Product not added.")

        elif option == "3":
            print("\nUpdate Stock")
            p_id = input("Enter Product ID: ").strip()
            product = inventory.find_product(p_id)
            if product is not None:
                print(f"Product Found: {product.get_name()} | Current Stock: {product.get_stock()}")
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
            product = inventory.find_product(p_id)
            if product is not None:
                print("\nProduct Found")
                print("-" * 35)
                print(product.display_information())
                print("-" * 35)
            else:
                print("Product not found.")

        elif option == "5":
            print("\nCreate New Order")
            order_id = input("Enter Order ID: ").strip()
            order = Order(order_id)
            
            while True:
                inv_p_id = input("Enter Product ID to add to order (or 'done' to finish): ").strip()
                if inv_p_id.lower() == 'done':
                    break
                product = inventory.find_product(inv_p_id)
                if product is not None:
                    try:
                        qty = int(input(f"Quantity for {product.get_name()}: ").strip())
                        order.add_order_line(product, qty)
                        print("Added to order.")
                    except ValueError:
                        print("Invalid quantity.")
                else:
                    print("Product not found in inventory.")
            
            order.display_order()

        elif option == "6":
            save_inventory(inventory)

        elif option == "7":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System. Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")