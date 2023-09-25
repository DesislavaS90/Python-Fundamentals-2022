data = input()

while True:

    command = input().split(' ')

    if command[0] == 'Done':
        break

    elif command[0] == 'Change':
        char, replacement = command[1], command[2]
        data = data.replace(char, replacement)
        print(data)

    elif command[0] == 'Includes':
        substring = command[1]
        if substring in data:
            print('True')
        else:
            print('False')

    elif command[0] == 'End':
        substring = command[1]
        if data.endswith(substring):
            print('True')
        else:
            print('False')

    elif command[0] == 'Uppercase':
        data = data.upper()
        print(data)

    elif command[0] == 'FindIndex':
        char = command[1]
        my_char = data.index(char)
        print(my_char)

    elif command[0] == 'Cut':
        start_index, count = int(command[1]), int(command[2])
        data = data[start_index:(start_index + count)]
        print(data)
