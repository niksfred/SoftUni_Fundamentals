n = int(input())

for rows in range(0, n+1):
    print("*"*rows)
for rows in range(n -1, 0, -1):
    print("*" * rows)

