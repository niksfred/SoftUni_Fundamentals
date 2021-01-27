chars_number = int(input())
result = 0
for i in range(0, chars_number):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}") 
