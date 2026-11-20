import unittest
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from product_factory import ProductFactory
from order import Order
from discount_strategies import PercentageDiscount, BulkDiscount

class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S01", "Test Supplier", "test@email.com")

    def test_factory_creates_correct_product(self):
        prod = ProductFactory.create("physical", "P01", "Laptop", 1000.0, 10, self.supplier, 2.5)
        self.assertIsInstance(prod, PhysicalProduct)
        
    def test_factory_raises_error_on_unknown(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S01", "Setup", 50.0, 1, self.supplier, 0.0)

    def test_validation_rejects_negative_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct("P02", "Desk", -10.0, 5, self.supplier, 10.0)

    def test_discount_strategies(self):
        order = Order("ORD1")
        prod = PhysicalProduct("P01", "Laptop", 1000.0, 10, self.supplier, 2.5)
        order.add_order_line(prod, 1)
        
        self.assertEqual(order.calculate_total(), 1000.0)
        
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 900.0)
        
        order.set_discount(BulkDiscount(500, 50))
        self.assertEqual(order.calculate_total(), 950.0)

if __name__ == '__main__':
    unittest.main()