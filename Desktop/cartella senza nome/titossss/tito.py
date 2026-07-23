class User:
    def __init__(self, name, email, is_active=True):
        self.name = name
        self.email = email
        self.is_active = is_active

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def describe(self):
        status = "Active" if self.is_active else "Inactive"
        return f"User: {self.name} | Email: {self.email} | Status: {status}"


class Product:
    
    store_name = "ShopWave Store"

    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

    def describe(self):
        stock_status = "In Stock" if self.in_stock else "Out of Stock"
        return f"Product: {self.name} | Price: ${self.price:.2f} | {stock_status} | Store: {Product.store_name}"



user1 = User("Ahmed", "ahmed@example.com")
user2 = User("Tito", "tito@example.com")
user3 = User("Sara", "sara@example.com")

prod1 = Product("Laptop", 1200.0)
prod2 = Product("Mouse", 25.5)
prod3 = Product("Keyboard", 75.0)
prod4 = Product("Monitor", 300.0)

user2.deactivate()
prod1.apply_discount(10)  

print("--- Users List ---")
print(user1.describe())
print(user2.describe())
print(user3.describe())

print("\n--- Products List ---")
products_list = [prod1, prod2, prod3, prod4]
for p in products_list:
    print(p.describe())
