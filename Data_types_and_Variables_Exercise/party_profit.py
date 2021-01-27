companion = int(input())
days_total = int(input())
profit = 0

for day in range(1, days_total + 1):
    if day % 15 == 0:
        companion += 5
    if day % 10 == 0:
        companion -= 2
    profit += 50
    profit -= (companion * 2)
    if day % 3 == 0:
        profit -= (companion * 3)
    if day % 5 == 0:
        profit += companion * 20
        if day % 3 == 0:
            profit -= companion * 2

print(f"{companion} companions received {int(profit/companion)} coins each.")
