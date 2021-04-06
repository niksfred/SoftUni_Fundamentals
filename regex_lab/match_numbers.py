import re

pattern = r"(^|(?<=\s))-?\d+(.\d+)?($|(?=\s))"

numbers = input()

matches = [obj.group() for obj in re.finditer(pattern, numbers)]

print(' '.join(matches))

