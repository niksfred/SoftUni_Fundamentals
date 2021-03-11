item_list = input().split("|")
budget = float(input())
purchases = []
profit = 0

for i in range(len(item_list)):
    item = item_list[i].split("->")
    category = item[0]
    price = float(item[1])
    
    if category == "Clothes":
        if not 0 < price <= 50:
            continue
    elif category == "Shoes":
        if not 0 < price <= 35:
            continue
    elif category == "Accessories":
        if not 0 < price <= 20.50:
            continue
    
    if budget < price:
        continue
    
    budget -= price
    profit += price * 0.4
    price_after_profit = price * 1.4
    purchases.append(price_after_profit)

for j in range(len(purchases)):
    print(f"{purchases[j]:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(purchases) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
