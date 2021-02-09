initial_string = input().split("#")
water = int(input())
valid_cells = []
total_fire = 0
effort = 0

for i in range(len(initial_string)):
    cell_check = initial_string[i].split(" = ")
    if cell_check[0] == "Low" and 1 <= int(cell_check[1]) <= 50:
        if water >= int(cell_check[1]):
            water -= int(cell_check[1])
            total_fire += int(cell_check[1])
            effort += int(cell_check[1]) * 0.25
            valid_cells.append(cell_check[1])
    
    elif cell_check[0] == "Medium" and 51 <= int(cell_check[1]) <= 80:
        if water >= int(cell_check[1]):
            water -= int(cell_check[1])
            total_fire += int(cell_check[1])
            effort += int(cell_check[1]) * 0.25
            valid_cells.append(cell_check[1])
    
    elif cell_check[0] == "High" and 81 <= int(cell_check[1]) <= 125:
        if water >= int(cell_check[1]):
            water -= int(cell_check[1])
            total_fire += int(cell_check[1])
            effort += int(cell_check[1]) * 0.25
            valid_cells.append(cell_check[1])

print("Cells:")
for j in range(len(valid_cells)):
    print(f" - {valid_cells[j]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
