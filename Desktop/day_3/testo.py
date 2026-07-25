class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.name} - ${self.__price}"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.__price == other.__price
        return False


class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} ({self.file_size}MB)"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.get_price() for item in self.items)

    def item_count(self):
        return len(self.items)


p1 = Product("Laptop", 1000)
p2 = DigitalProduct("E-Book", 20, 5)

cart = Cart()
cart.add_item(p1)
cart.add_item(p2)

catalog = [p1, p2]
for item in catalog:
    print(item)

print("Total:", cart.total())
print("Count:", cart.item_count())
