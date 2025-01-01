products = {
    "Apples": 1.50,
    "Bananas": 0.75,
    "Oranges": 0.80,
    "Milk": 1.20,
    "Bread": 1.00
}

total_cost = 0
for product, price in products.items():
    print(f"{product}: ${price:.2f}")
    total_cost += price

print(f"Total cost of all products: ${total_cost:.2f}")
