words_input = input().split()
dic = {}

for el in words_input:
    el_lower = el.lower()
    if not el_lower in dic:
        dic[el_lower] = 0
    dic[el_lower] += 1

for key, value in dic.items():
    if not value % 2 == 0:
        print(key, end=" ")
