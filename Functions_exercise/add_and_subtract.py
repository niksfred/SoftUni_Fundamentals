
def add_and_subtract(num1, num2, num3):
    result = None
    result = num1 + num2
    result -= num3
    return result

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
