trains_number = int(input())
trains = [0] * trains_number

command = input()
while not command == "End":
    commmands = command.split()
    if "add" in commmands:
        people = int(commmands[1])
        trains[-1] += people
    elif "insert" in commmands:
        people = int(commmands[2])
        index = int(commmands[1])
        trains[index] += people
    elif "leave" in commmands:
        people = int(commmands[2])
        index = int(commmands[1])
        trains[index] -= people

    command = input()
print(trains)
