elements = input().split()
products = {}

for i in range(0, len(elements), 2):
    current_product = elements[i]
    quantity = int(elements[i+1])
    products[current_product] = quantity

search_input = input().split()
for element in search_input:
    if element in products:
        print(f"We have {products[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
