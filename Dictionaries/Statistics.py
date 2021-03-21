command = input()
products = {}

while not command == "statistics":
    key, value = command.split(": ")
    if not key in products:
        products[key] = int(value)
    else:
        products[key] += int(value)
    
    command = input()
    
print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
