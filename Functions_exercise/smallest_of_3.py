import sys

def min_num(n1,n2,n3):
    result = sys.maxsize
    if n1 < result:
        result = n1
    if n2 < result:
        result = n2
    if n3 < result:
        result = n3
    return result

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(min_num(number_1, number_2, number_3))
