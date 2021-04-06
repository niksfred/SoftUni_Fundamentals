string = input()

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        string = string.replace(char, replacement)
        print(string)

    elif command[0] == "Includes":
        if command[1] in string:
            print("True")
        else:
            print("False")
    
    elif command[0] == "Start":
        check = command[1]
        print(string.startswith(check))

    elif command[0] == "Lowercase":
        string = string.lower()
        print(string)
    
    elif command[0] == "FindIndex":
        char = command[1]
        print(string.rindex(char))

    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string = string[0 : start_index : ] + string[start_index + count : :]
        print(string)
    
    command = input()
