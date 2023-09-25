coffee_count = 0

while True:
    commands = input()

    if commands == 'END':
        break

    if commands == 'coding' or commands == 'cat' or commands == 'dog' or commands == 'movie':
        coffee_count += 1
    elif commands == 'coding'.upper() or commands == 'cat'.upper() \
            or commands == 'dog'.upper() or commands == 'movie'.upper():
        coffee_count += 2
    else:
        continue

if coffee_count > 5:
    print('You need extra sleep')

else:
    print(coffee_count)


