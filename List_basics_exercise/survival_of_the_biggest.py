numbers_string = input()
numbers_to_remove = int(input())

numbers_list = numbers_string.split(" ")
numbers_list = list(map(int, numbers_list))
for i in range(numbers_to_remove):
    numbers_list.remove(min(numbers_list))
print(numbers_list)
