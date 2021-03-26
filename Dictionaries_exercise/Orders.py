data = input()

products = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["price"] = price
        products[name]["quantity"] += quantity

    data = input()

for key, value in products.items():
    result = products[key]["price"] * products[key]["quantity"]
    print(f"{key} -> {result:.2f}")
