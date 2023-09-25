wagon_length = int(input())

wagons = [0] * wagon_length

while True:
    command = input()

    if command == 'End':
        break
    my_command = command.split()

    if my_command[0] == 'add':
        number_people = int(my_command[1])
        wagons[-1] += number_people
    elif my_command[0] == 'insert':
        index = int(my_command[1])
        people = int(my_command[2])
        wagons[index] += people
    elif my_command[0] == 'leave':
        index = int(my_command[1])
        people_to_add = int(my_command[2])
        wagons[index] -= people_to_add

print(wagons)
