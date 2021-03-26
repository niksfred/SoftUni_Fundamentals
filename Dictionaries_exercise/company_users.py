data = input()

companies = {}

while not data == "End":
    name, employee = data.split(" -> ")
    if name not in companies:
        companies[name] = []
    if employee not in companies[name]:
        companies[name].append(employee)

    data = input()

sorted_companies = sorted(companies.items(), key=lambda x: x[0])
for key, value in sorted_companies:
    print(key)
    for i in range(len(value)):
        print(f"-- {value[i]}")
