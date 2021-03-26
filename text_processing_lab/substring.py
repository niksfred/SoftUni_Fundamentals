del_str = input()
str = input()
while True:
    if del_str in str:
        str = str.replace(del_str, "")
    
    else:
        print(str)
        break
