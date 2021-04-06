data = input()
book = {}
while not data == "Lumpawaroo":
    if "|" in data:
        side, user = data.split(" | ")
        if user in book.values():
            pass
        elif user not in book.values():
            if side not in book:
                book[side] = [] 
            book[side].append(user)
    
    elif "->" in data:
        if user not in book.values():
            if side not in book:
                book[side] = [] 
            book[side].append(user)
            print(f"{user} joins the {side} side!" )
        elif user in book.values():
            pass

    data = input()