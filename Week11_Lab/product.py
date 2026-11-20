from abc import ABC, abstractmethod
from supplier import Supplier

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = float(price)
        self.__stock: int = int(stock_quantity)
        self.supplier: Supplier = supplier

    def update_stock(self, new_quantity: int) -> None:
        self.__stock = int(new_quantity)

    def display_information(self) -> str:
        return f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock} | {self.supplier.display_information()}"

    def get_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_stock(self) -> int:
        return self.__stock

    def get_price(self) -> float:
        return self.__price

    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier_id": self.supplier.supplier_id,
            "supplier_name": self.supplier.name,
            "supplier_email": self.supplier.contact_email
        }

    @abstractmethod
    def get_fullment_info(self) -> str:
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.__weight: float = float(weight)

    def display_information(self) -> str:
        return f"{super().display_information()} | Weight: {self.__weight} kg"

    def get_fullment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5.00

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.__download_size: float = float(download_size)

    def display_information(self) -> str:
        return f"{super().display_information()} | Download Size: {self.__download_size} MB"

    def get_fullment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data