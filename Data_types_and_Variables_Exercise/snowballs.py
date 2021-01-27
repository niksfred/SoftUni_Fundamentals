import sys
result_snowball_value = -sys.maxsize
result_snowball_snow = None
result_snowball_time = None
result_snowball_quality = None
snowballs = int(input())

for i in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > result_snowball_value:
        result_snowball_value = snowball_value
        result_snowball_quality = snowball_quality
        result_snowball_snow = snowball_snow
        result_snowball_time = snowball_time

print(f"{result_snowball_snow} : {result_snowball_time} = {int(result_snowball_value)} ({result_snowball_quality})")
