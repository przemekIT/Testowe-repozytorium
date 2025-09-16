from functools import reduce

orders = [
    {"product": "Laptop", "price": 3500, "quantity": 2},
    {"product": "Mouse", "price": 80, "quantity": 5},
    {"product": "Keyboard", "price": 200, "quantity": 90},
    {"product": "Monitor", "price": 900, "quantity": 2},
]

# Łączna wartosc zamowien
total_value = reduce(lambda acc, order: acc + order["price"] * order["quantity"], orders, 0)

# Znajdz zamowienie o najwiekszej wartosci
max_order = reduce(lambda acc, order: order if (order["price"] * order["quantity"]) > (acc["price"] * acc["quantity"]) else acc, orders)

print(f"Łączna wartość zamowien: {total_value} zł")
print(f"Produkt o najwyzszej wartosci zamowienia: {max_order['product']}", f"({max_order['price'] * max_order['quantity']}) zł")