def range_chars(char_1, char_2):
    range_start = ord(char_1)
    range_end = ord(char_2)

    for i in range(range_start+ 1, range_end):
        print(chr(i), end=" ")
    
character_1 = input()
character_2 = input()

range_chars(character_1, character_2)
