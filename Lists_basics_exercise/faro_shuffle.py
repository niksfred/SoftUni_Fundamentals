cards = input()
shuffles_number = int(input())
shuffled_list = []
cards_order = cards.split(" ")
deck_split = int(len(cards_order) / 2)
for i in range(1, shuffles_number + 1):
    for j in range(deck_split):
        element = cards_order[j]
        shuffled_list.append(element)
        element = cards_order[(deck_split + j)]
        shuffled_list.append(element)
    if not i == shuffles_number:
        cards_order = shuffled_list
        shuffled_list = []
print(shuffled_list)
