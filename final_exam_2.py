import re

str_number = int(input())

pattern = r"^(\W|\S+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(\W|\S{3})<\1"

for tries in range(str_number):
    password = input()
    
    if re.match(pattern, password):
        match = re.match(pattern, password)
        print(f"Password: {match[2]}{match[3]}{match[4]}{match[5]}")
    
    else:
        print("Try another password!")
