word = input()
index_list = []

for index in range(len(word)):
    if word[index].isupper():
        index_list.append(index)

print(index_list)
