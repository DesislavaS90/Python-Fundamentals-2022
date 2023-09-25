parking = {}

number_of_cars = int(input())

for car in range(number_of_cars):
    command = input().split()
    current_command = command[0]

    if current_command == 'register':
        name, plate = command[1], command[2]
        if name in parking:
            print(f'ERROR: already registered with plate number {plate}')
        else:
            parking[name] = plate
            print(f'{name} registered {plate} successfully')
    else:
        name = command[1]
        if name not in parking:
            print(f'ERROR: user {name} not found')
        else:
            print(f'{name} unregistered successfully')
            del parking[name]

for username, plate in parking.items():
    print(f'{username} => {plate}')