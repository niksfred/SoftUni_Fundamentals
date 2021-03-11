import sys
def exchange(index_str,array):
    index = int(index_str)
    array_lenght = len(array)
    exchanged_array = []
    array_1 = array[index+1:]
    array_2 = array[:index+1]
    exchanged_array = array_1 + array_2
    return exchanged_array

def max_function(parameter, array):
    if parameter == "even":
        num = -sys.maxsize
        for i in range(len(array)-1, -1, -1):
            if array[i] % 2 == 0 and array[i] > num:
                num = array[i]
        if num in array:
            array.reverse()
            i = array.index(num)
            array.reverse()
            return len(array) - i - 1
        else:
            return "No matches"

    elif parameter == "odd":
        num = -sys.maxsize
        for i in range(len(array)):
            if not array[i] % 2 == 0 and array[i] > num:
                num = array[i]
        if num in array:
            return array.index(num)
        else:
            return "No matches"
                
def min_function(parameter, array):
    if parameter == "even":
        num = sys.maxsize
        for i in range(len(array)):
            if array[i] % 2 == 0 and array[i] < num:
                num = array[i]
        if num in array:
            array.reverse()
            i = array.index(num)
            array.reverse()
            return len(array) - i - 1
        else:
            return "No matches"

    elif parameter == "odd":
        num = sys.maxsize
        for i in range(len(array)):
            if not array[i] % 2 == 0 and array[i] < num:
                num = array[i]
        if num in array:    
            return array.index(num)
        else:
            return "No matches"

def first_num(parameter, count, array):
    if not count > len(array):
        num_list = []
        if parameter == "even":
            for i in range(len(array)):
                if len(num_list) < count and array[i] % 2 == 0:
                    num_list.append(array[i])
            return num_list
        elif parameter == "odd":
            for i in range(len(array)):
                if len(num_list) < count and not array[i] % 2 == 0:
                    num_list.append(array[i])
            return num_list
    else:
        return "Invalid count"

def last_num(parameter, count, array):
    if not count > len(array):
        num_list = []
        if parameter == "even":
            for i in range(len(array)-1, -1, -1):
                if len(num_list) < count and array[i] % 2 == 0:
                    num_list.insert(0,array[i])
            return num_list
        elif parameter == "odd":
            for i in range(len(array)-1, -1, -1):
                if len(num_list) < count and not array[i] % 2 == 0:
                    num_list.insert(0,array[i])
            return num_list
    else:
        return "Invalid count"

            
string_list = input()
initial_array = string_list.split(" ")
initial_array = list(map(int, initial_array))
command = input()
while not command == "end":
    command_list = command.split(" ")
    if "exchange" in command_list:
        if not int(command_list[1]) > len(initial_array):
            initial_array = exchange(command_list[1], initial_array)
        else:
            print("Invalid index")
    elif "max" in command_list:
        print(max_function(command_list[1],initial_array))
    elif "min" in command_list:
        print(min_function(command_list[1],initial_array))
    elif "first" in command_list:
        print(first_num(command_list[2], int(command_list[1]),initial_array))
    elif "last" in command_list:
        print(last_num(command_list[2], int(command_list[1]),initial_array))

    command = input()

print(initial_array)
