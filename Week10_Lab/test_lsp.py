from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

def show_product_details(product) -> None:
    print(product.display_information())
    print(product.get_fullment_info())
    print("-" * 20)

# Create a supplier
sup = Supplier("S001", "TechCorp", "contact@techcorp.com")

# Create Products (Polymorphism)
p1 = PhysicalProduct("P001", "Laptop", 1200.00, 10, sup, 2.5)
p2 = DigitalProduct("P002", "Antivirus", 50.00, 100, sup, 500.0)

print("=== LSP & POLYMORPHISM TEST ===")
# The same function handles different types seamlessly!
show_product_details(p1)
show_product_details(p2)

# Aggregation test: Add to inventory and remove
inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)
print("Inventory before removal:")
inv.display_all()

inv.remove_product("P001")
print("\nInventory after removing Laptop:")
inv.display_all()
print("Notice the Laptop object still exists independently (LSP & Aggregation preserved).")