def validator(password):
    digits_num = 0
    is_alphanumeric = password.isalnum()
    
    if 6<= len(password) <= 10:
        is_valid_leght = True
    else:
        is_valid_leght = False
    
    for i in range(len(password)):
        if password[i].isdigit():
            digits_num += 1
    
    if is_alphanumeric == True and is_valid_leght == True and digits_num >= 2:
        print("Password is valid")
    else:
        if not is_valid_leght:
            print("Password must be between 6 and 10 characters")
        if not is_alphanumeric:
            print("Password must consist only of letters and digits")
        if not digits_num >= 2:
            print("Password must have at least 2 digits")

password = input()
validator(password)
