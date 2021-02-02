n = int(input())
numbers_list = []
filtered = []

for i in range(1, n + 1):
    number = int(input())
    numbers_list.append(number)

command = input()

if command == "even":
    for number in numbers_list:
        if number % 2 == 0:
            filtered.append(number)
        
       
elif command == "odd":
    for number in numbers_list:
        if not number % 2 == 0:
            filtered.append(number)

elif command == "negative":
    for number in numbers_list:
        if number  < 0:
            filtered.append(number)

elif command == "positive":
    for number in numbers_list:
        if number  >= 0:
            filtered.append(number)

print(filtered)

