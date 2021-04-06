str = input()
result = ""
for char in str:
     if char.isdigit():
        result += char
        
print(result)
result = ""  

for char in str:
    if char.isalpha():
        result += char

print(result)
result = ""  

for char in str:
    if not char.isdigit() and not char.isalpha():
        result += char
print(result)


