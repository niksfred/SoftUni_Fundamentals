def validator(password):
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
            print("Password must have at least 2 digits")

password = input()
validator(password)
