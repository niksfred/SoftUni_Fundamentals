def fac_div(num1, num2):
    fac_num1 = 1
    for i in range(1, num1 +1):
        fac_num1 = fac_num1 * i
    
    fac_num2 = 1
    for j in range(1, num2 + 1):
        fac_num2 = fac_num2 * j

    result = fac_num1 / fac_num2
    return result

number_1 = int(input())
number_2 = int(input())

print(f"{fac_div(number_1, number_2):.2f}")
