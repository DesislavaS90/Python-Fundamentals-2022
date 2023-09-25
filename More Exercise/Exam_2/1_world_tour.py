stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    current_command = command.split(':')

    if current_command[0] == 'Add Stop':
        index, string = int(current_command[1]), current_command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
            print(stops)
        else:
            print(stops)

    elif current_command[0] == 'Remove Stop':
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            start = stops[:start_index]
            end = stops[end_index + 1:]
            stops = start + end
            print(stops)
        else:
            print(stops)

    elif current_command[0] == 'Switch':
        old_string, new_string = current_command[1], current_command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
            print(stops)
        else:
            print(stops)
print(f'Ready for world tour! Planned stops: {stops}')


# "Add Stop:{index}:{string}":
# Insert the given string at that index only if the index is valid

# "Remove Stop:{start_index}:{end_index}":
# Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid

# "Switch:{old_string}:{new_string}":
# If the old string is in the initial string, replace it with the new one (all occurrences)
