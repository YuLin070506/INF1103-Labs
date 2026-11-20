from order_line import OrderLine
from product import Product
from discount_strategies import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        # Order creates the OrderLine internally (Composition)
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.order_lines:
            total += line.calculate_subtotal()
        
        # This line is crucial! It applies the strategy.
        return self.discount.apply(total) 

    def display_order(self) -> None:
        print(f"\n--- Order ID: {self.order_id} ---")
        for line in self.order_lines:
            print(line.display_line())
        print(f"Total Order Value: ${self.calculate_total():.2f}")