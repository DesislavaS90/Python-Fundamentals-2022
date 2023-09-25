my_list = []

while True:
    command = input()

    if command == 'End':
        break
    notes = command.split('-')
    priority = int(notes[0])
    task = notes[1]
    my_list.append([priority, task])
    sorted_list = [i[1] for i in sorted(my_list)]

print(sorted_list)
