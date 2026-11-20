from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

    def display_line(self) -> str:
        return f"{self.product.get_name()} (x{self.quantity}) - Subtotal: ${self.calculate_subtotal():.2f}"