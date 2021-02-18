def calculator(num1, num2, operator):
    result = None
    if operator == "multiply":
        result = num1 * num2
        return result
    elif operator == "divide":
        result = num1 / num2
        return result
    elif operator == "add":
        result = num1 + num2
        return result
    elif operator == "subtract":
        result = num1 - num2
        return result

operator_input = input()
number_1 = int(input())
number_2 = int(input())

print(f"{calculator(number_1, number_2, operator_input):.0f}")
