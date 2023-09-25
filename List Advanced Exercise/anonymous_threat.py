text = input().split()  # Ivo Johny Tony Bony Mony

my_list = []

while True:
    command = input()
    if command == "3:1":
        break

    current_command = command.split()

    if current_command[0] == 'merge':
        start, end = int(current_command[1]), int(current_command[2])




