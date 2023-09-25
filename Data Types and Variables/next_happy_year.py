year = int(input())

counter = year
happy_year = ''
str_counter = ''

for i in range(year):
    counter += 1
    str_counter = str(counter)
    happy_year = set((str(counter)))

    if len(str_counter) == len(happy_year):
        break
print(counter)



