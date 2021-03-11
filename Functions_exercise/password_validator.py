def validator(password):
<<<<<<< HEAD
    valid_password_lenght = True
    valid_password_composition = True
    digit_counter = 0
    
    for i in password:
        char = ord(i)
        if not 47 < char < 58 or 64 < char < 91 or 96 < char < 123:
            valid_password_composition = False
            break
    for i in password:
        char = ord(i)
        if 47 < char < 58:
            digit_counter =+ 1
    
    if not 6 <= len(password) <= 10:
        valid_password_lenght = False

    if valid_password_lenght == True and valid_password_composition == True and digit_counter >= 2:
        print("Password is valid")
    else:
        if not valid_password_lenght:
            print("Password must be between 6 and 10 characters")
        if not valid_password_composition:
            print("Password must consist only of letters and digits")
        if digit_counter < 2:
=======
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
>>>>>>> 1f1cb2a892d60c80c4074f210aa4f645416b2053
            print("Password must have at least 2 digits")

password = input()
validator(password)
