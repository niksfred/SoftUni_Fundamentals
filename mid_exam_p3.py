cards = [x for x in input().split(":")]
deck = []

command = input()

while not command == "Ready":
    data = command.split()

    if "Add" in data:
        if data[1] in cards:
            deck.append(data[1])
        else:
            print("Card not found.")
    elif "Insert" in data:
        if 0 <= int(data[2]) <= len(deck) and data[1] in cards:
            deck.insert(int(data[2]), data[1])
        else:
            print("Error!")
    elif "Remove" in data:
        if data[1] in deck:
            deck.remove(data[1])
        else:
            print("Card not found.")
    elif "Swap" in data:
        index1 = deck.index(data[1])
        index2 = deck.index(data[2])
        deck[index1], deck[index2] = deck[index2], deck[index1]

    elif "Shuffle" in data:
        deck.reverse()
    
    command = input()

for i in range(len(deck)):
    print(deck[i], end=" ")

