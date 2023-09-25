budget = int(input())

counter = 0

while True:
    command = input()

    if command == 'End':
        break

    price = int(command)
    counter += price

    if budget < counter:
        break

if budget < counter:
    print('You went in overdraft!')

else:
    print('You bought everything needed.')


