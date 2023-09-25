houses = list(map(int, input().split('@')))

index = 0

while True:
    command = input().split()
    action = command[0]

    if action == 'Love!':
        break

    if action == 'Jump':

        index += int(command[1])
        if index >= len(houses):
            index = 0
        if houses[index] == 0:
            print(f'Place {index} already had Valentine\'s day.')
        else:
            houses[index] -= 2
            if houses[index] == 0:
                print(f'Place {index} has Valentine\'s day.')
    else:
        break


print(f'Cupid\'s last position was {index}.')

counter = 0
for num in houses:
    if num > 0:
        counter += 1
if counter > 0:
    print(f'Cupid has failed {counter} places.')
else:
    print(f'Mission was successful.')
