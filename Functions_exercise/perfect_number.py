def is_perfect_num(number):
    sum_divisors = 0
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            sum_divisors += i   
    if sum_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
is_perfect_num(number)
