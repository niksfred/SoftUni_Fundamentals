gifts = input().split()
current_command_string = input()

while not "No Money" == current_command_string:
    current_command = current_command_string.split()
    gift = current_command[1]

    if current_command[0] == "OutOfStock":
        for n in range(len(gifts)):
            if gifts[n] == gift:
                gifts[n] = "None"

    elif current_command[0] == "Required":
        position = int(current_command[2])
        if 0 <= position < len(gifts):
            gifts[position] = gift

    elif current_command[0] == "JustInCase":
        gifts[-1] = gift
    current_command_string = input()

for gift in gifts:
    if not gift == "None":
        print(gift, end=" ")
