import re

text = input()

pattern = f"\d+"
numbers = []
while not text == "":

    matches = re.findall(pattern, text)
    for match in matches:
        numbers.append(match)
    text = input()

print(' '.join(numbers))
