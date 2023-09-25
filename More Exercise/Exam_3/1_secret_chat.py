concealed_message = input()

while True:

    command = input()

    if command == 'Reveal':
        break

    current_command = command.split(':|:')

    if current_command[0] == 'InsertSpace':
        index = int(current_command[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)

    elif current_command[0] == 'Reverse':
        substring = current_command[1]
        if substring in concealed_message:
            new_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += new_substring
            print(concealed_message)
        else:
            print('error')

    elif current_command[0] == 'ChangeAll':
        substring, replacement = current_command[1], current_command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f'You have a new text message: {concealed_message}')



# "InsertSpace:|:{index}":
# Inserts a single space at the given index. The given index will always be valid.

# "Reverse:|:{substring}":
# If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# If not, print "error".
# This operation should replace only the first occurrence of the given substring if there are two or more occurrences.

# "ChangeAll:|:{substring}:|:{replacement}":
# Changes all occurrences of the given substring with the replacement text.
