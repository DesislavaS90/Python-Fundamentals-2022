
while True:
    command = input()
    word = ''

    if command == 'SoftUni':
        continue

    if command == 'End':
        break

    for char in command:
        word += char*2

    print(word)
