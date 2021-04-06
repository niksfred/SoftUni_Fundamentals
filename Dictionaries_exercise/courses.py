data = input()

courses = {}
while not data == "end":
    name, person = data.split(" : ")

    if name not in courses:
        courses[name] = []
    courses[name].append(person)

    data = input()

sorted_courses = sorted(courses.items(), key=lambda x: -len(x[1]))
for key, value in sorted_courses:
    value.sort()
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
