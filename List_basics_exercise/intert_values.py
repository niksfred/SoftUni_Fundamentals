string = input()
opposite_string = []
stringlist= string.split(" ")
for i in range(len(stringlist)):
    element = int(stringlist[i])
    opposite_string.append(-element)

print(opposite_string)
