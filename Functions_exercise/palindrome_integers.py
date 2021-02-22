def palindrome(numbers_string):
    numbers_list = numbers_string.split(", ")

    for number in numbers_list:
        reversed_number ="".join(reversed(number))
        if number == reversed_number:
            print("True")
        else:
            print("False")

numbers_string = input()
palindrome(numbers_string)

