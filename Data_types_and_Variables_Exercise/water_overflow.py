lines_number = int(input())
current_volume = 0
tank_capacity = 255


for i in range(lines_number):
    pour_volume = int(input())
    current_volume += pour_volume
    if current_volume > 255:
        print("Insufficient capacity!")
        current_volume -= pour_volume

print(current_volume)
