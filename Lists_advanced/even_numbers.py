initial_numbers = input().split(", ")
even_list = []
for i in range(len(initial_numbers)):
    if int(initial_numbers[i]) % 2 == 0:
        even_list.append(i)
print(even_list)
