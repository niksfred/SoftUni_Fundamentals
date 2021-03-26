resource = input()

resources_collection = {}

while not resource == "stop":
    quantity = int(input())
    if not resource in resources_collection:
        resources_collection[resource] = 0
    resources_collection[resource] += quantity

    resource = input()

for key, value in resources_collection.items():
    print(f"{key} -> {value}")
