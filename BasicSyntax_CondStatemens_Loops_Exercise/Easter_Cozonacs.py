budget = float(input())
flour_price = float(input())
colored_eggs_counter = 0
cozonacs = 0
third_cozonac = 0

egg_pack = flour_price * 0.75
liter_of_milk = flour_price * 1.25
quarter_milk = liter_of_milk / 4
cozonac_price = egg_pack + flour_price + quarter_milk

while budget > cozonac_price:
    budget -= cozonac_price
    cozonacs += 1
    colored_eggs_counter += 3
    third_cozonac += 1
    if third_cozonac == 3:
        colored_eggs_counter -= cozonacs - 2
        third_cozonac = 0

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
