word = input()
chars = {}

for char in word:
    if char == " ":
        continue
    elif char not in chars:
        chars[char] = 0
    chars[char] += 1

for key, value in chars.items():
    print(f"{key} -> {value}")
