numbers = []
factor = int(input())
count = int(input())

for i in range(1, count + 1):
    item = i * factor
    numbers.append(item)

print(numbers)