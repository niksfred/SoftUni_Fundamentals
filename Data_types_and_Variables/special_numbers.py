number = int(input())

sum_of_digits = 0
for i in range(1, number+1):
    for digit in str(i):
        sum_of_digits += int(digit)
    if (sum_of_digits == 5) or (sum_of_digits  == 7) or (sum_of_digits == 11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
    sum_of_digits = 0
    