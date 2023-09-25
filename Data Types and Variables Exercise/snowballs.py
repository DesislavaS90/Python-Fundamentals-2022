number_of_snowballs = int(input())

snowball_weight = 0
snowball_time = 0
snowball_value = 0
snowball_quality = 0


for i in range(number_of_snowballs):
    weigh = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weigh / time_needed) ** quality
    if value > snowball_value:
        snowball_weight = weigh
        snowball_time = time_needed
        snowball_value = value
        snowball_quality = quality
print(f'{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})')
