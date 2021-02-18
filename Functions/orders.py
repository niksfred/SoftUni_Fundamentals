coffee = 1.50
water = 1
coke = 1.40
snacks = 2.00

def orders(item, quantity):
    result = None
    if item == "coffee":
        result = coffee * quantity
        return result
    elif item == "water":
        result = water * quantity
        return result
    elif item == "coke":
        result = coke * quantity
        return result
    elif item == "snacks":
        result = snacks * quantity
        return result

item_input = input()
quantity_input = int(input())

print(f"{orders(item_input, quantity_input):.2f}")
