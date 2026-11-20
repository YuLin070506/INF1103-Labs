from product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: str) -> None:
        for i, product in enumerate(self.products):
            if product.get_id() == product_id:
                del self.products[i]
                return

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        if len(self.products) == 0:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory")
        print("-" * 35)
        for product in self.products:
            print(product.display_information())
        print("-" * 35)