elements = input().split()
products = {}

for i in range(0, len(elements), 2):
    current_product = elements[i]
    quantity = int(elements[i+1])
    products[current_product] = quantity

print(products)
