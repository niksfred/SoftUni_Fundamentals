line_list = []
n = int(input())
word = input()

for i in range(1, n + 1):
    line = input()
    line_list.append(line)

print(line_list)
for i in range(len(line_list)-1, -1, -1):
    element = line_list[i]
    if word not in element:
        line_list.remove(element)
print(line_list)
 