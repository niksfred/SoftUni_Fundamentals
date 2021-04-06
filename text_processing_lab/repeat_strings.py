list = input().split()
result = ""
for word in list:
    result += word * len(word)

print(result)