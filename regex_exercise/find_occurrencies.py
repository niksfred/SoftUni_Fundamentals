import re

text = input().lower()

pattern = f"{input()}\\b"

matches = re.findall(pattern, text)

print(len(matches))
