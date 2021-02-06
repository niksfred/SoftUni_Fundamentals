numbers_string = input()
beggars = int(input())
beggars_sum = []
for i in range (beggars):
    beggars_sum.append(0)
beggar_turn = 0
numbers_list = numbers_string.split(", ")
for element in numbers_list:
    element_value = int(element)
    beggars_sum[beggar_turn] += element_value
    beggar_turn += 1
    if beggar_turn == beggars:
        beggar_turn = 0

print(beggars_sum)
