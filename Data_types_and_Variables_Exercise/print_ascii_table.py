ascii_table_start = int(input())
ascii_table_end = int(input())
result_string = ""

for i in range(ascii_table_start, ascii_table_end + 1):
    result_string += chr(i)
    result_string += " "

print(result_string)
