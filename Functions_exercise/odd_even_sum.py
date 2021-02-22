def odd_even_sum(string_number):
    odd_sum = 0
    even_sum = 0
    
    for i in string_number:
        number = int(i)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

string = input()
odd_even_sum(string)
