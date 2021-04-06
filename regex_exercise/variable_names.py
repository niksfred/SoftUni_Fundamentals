import re

text = input()

pattern = r"\b_([a-z]|[A-Z])+\b"

variables_groups = [obj.group() for obj in re.finditer(pattern, text)]
variables = [v[1:] for v in variables_groups]

print(','.join(variables))
