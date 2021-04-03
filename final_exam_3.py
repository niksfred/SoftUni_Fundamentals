from typing import Coroutine


command = input()
followers = {}
while not command == "Log out":
    command = command.split(": ")
    
    if command[0] == "New follower":
        user = command[1]
        if not user in followers:
            followers[user] = {"likes": 0, "comments": 0}
        
    elif command[0] == "Like":
        user = command[1]
        count = int(command[2])
        if not user in followers:
            followers[user] = {"likes": 0, "comments": 0}
        followers[user]["likes"] += count

    elif command[0] == "Comment":
        user = command[1]
        if not user in followers:
            followers[user] = {"likes": 0, "comments": 0}
        followers[user]["comments"] += 1

    elif command[0] == "Blocked":
        user = command[1]

        if user in followers:
            followers.pop(user)
        else:
            print(f"{user} doesn't exist.")

    command = input()

dic = {}
for user in followers:
    dic[user] = sum(followers[user].values())

sorted_list = sorted(dic.items(), key= lambda x: (-x[1], x[0]))

print(f"{len(followers)} followers")
for key, value in sorted_list:
    print(f"{key}: {value}")
