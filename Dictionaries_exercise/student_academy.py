n = int(input())

dic = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if not name in dic:
        dic[name] = []
    dic[name].append(grade)

above_average = {}

for key,value in dic.items():
    result = sum(value)/len(value)
    if result  >= 4.50:
        above_average[key] = result

sorted_dic = sorted(above_average.items(), key=lambda x: x[1], reverse=True)
for key, value in sorted_dic:
    print(f"{key} -> {value:.2f}")
    