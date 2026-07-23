products = [
    {"name": "Wireless Mouse", "price": 25.99, "in_stock": 5},
    {"name": "Mechanical Keyboard", "price": 75.50, "in_stock": 2},
    {"name": "Gaming Monitor", "price": 199.99, "in_stock": 0},
    {"name": "USB-C Hub", "price": 15.00, "in_stock": 10},
    {"name": "Laptop Stand", "price": 35.49, "in_stock": 4}
]

def describe(product):
    price = product["price"]
    if price < 30.0:
        label = "cheap"
    elif price <= 100.0:
        label = "mid"
    else:
        label = "expensive"
    
    return f"Product: {product['name']} | Price: ${price:.2f} | Category: {label} | Stock: {product['in_stock']}"

def total_value(products):
    total = 0.0
    for product in products:
        total += product["price"]
    return total

def count_in_stock(products):
    count = 0
    for product in products:
        if product["in_stock"] > 0:
            count += 1
    return count

print("--- Product Descriptions ---")
for product in products:
    print(describe(product))

print("\n--- Statistics ---")
print(f"Total Catalog Value: ${total_value(products):.2f}")
print(f"Products in stock: {count_in_stock(products)}")

print("\n--- Stock Countdown Simulation ---")
countdown = 3
while countdown >= 0:
    print(f"Countdown: {countdown}")
    countdown -= 1