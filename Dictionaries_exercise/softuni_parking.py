n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    if command[0] == "register":
        name = command[1]
        vehicle = command[2]
        if name not in parking:
            parking[name] = vehicle
            print(f"{name} registered {parking[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")

    elif command[0] == "unregister":
        name = command[1]
        if name in parking:
            parking.pop(name, None)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, value in parking.items():
    print(f"{key} => {value}")

