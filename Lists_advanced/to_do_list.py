to_do_list = [0] * 10

command = input()

while not command == "End":
    priority, note = command.split("-")
    priority = int(priority) - 1
    to_do_list[priority] = note
    command = input()

print([task for task in to_do_list if not task == 0])
