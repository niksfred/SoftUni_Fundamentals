cubes = [int(x) for x in input().split()]
command = input()

while not command == "Mort":
    data = command.split()
    if "Add" in data:
        cubes.append(int(data[1]))
    elif "Remove" in data:
        cubes.remove(int(data[1]))
    elif "Replace" in data:
        for i in range(len(cubes)):
            if cubes[i] == int(data[1]):
                cubes[i] = int(data[2])
                break
    elif "Collapse" in data:
        for i in range(len(cubes)-1, -1,-1):
            if cubes[-i] < int(data[1]):
                cubes.pop(-i)
    command = input()

for i in cubes:
    print(i, end=" ")

