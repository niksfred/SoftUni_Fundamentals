del_str = input().split(", ")
str = input()

for word in del_str:
        str = str.replace(word, "*" * len(word))

print(str)