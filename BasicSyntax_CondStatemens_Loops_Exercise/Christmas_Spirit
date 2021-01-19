quantity = int(input())
days = int(input())
spirit = 0
budget = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5
    if i % 3 == 0:
        budget += tree_skirt * quantity
        budget += tree_garlands * quantity
        spirit += 13
    if i % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += tree_garlands + tree_lights + tree_skirt

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
