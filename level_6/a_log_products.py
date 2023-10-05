"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знает о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""

class PrintLoggerMixin:
    def log(self, message: str) -> None:
        print(f"Log: {message}")


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.log(f'Price increased from {self.price} to {self.price * 1.2}')
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        self.log(f'Premium product info: {base_info}')
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.log(f'Price decreased from {self.price} to {self.price / 1.2}')
        self.price /= 1.2

    def get_info(self):
        base_info = super().get_info()
        self.log(f'Discounted product info: {base_info}')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    product = PremiumProduct('Banana', 100.1)
    product.increase_price()
    print(product.get_info())

    product = DiscountedProduct('Slama', 250.2)
    product.increase_price()
    print(product.get_info())

