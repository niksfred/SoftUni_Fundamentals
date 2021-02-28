orders_count = int(input())
coffee_prices = []

for i in range(orders_count):
    price_per_capsule = float(input())
    days_in_month = int(input())
    capsules_count = int(input())
    price = ((days_in_month * capsules_count) * price_per_capsule)
    coffee_prices.append(price)

for i in range(orders_count):
    print(f"The price for the coffee is: ${coffee_prices[i]:.2f}")
print(f"Total: ${sum(coffee_prices):.2f}")
