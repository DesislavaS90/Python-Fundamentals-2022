encrypted_message = input()

while True:

    command = input().split('|')

    if command[0] == 'Decode':
        break

    elif command[0] == 'Move':
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif command[0] == 'Insert':
        index, value = int(command[1]), command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)

print(f'The decrypted message is: {encrypted_message}')

# "Move {number of letters}":
# Moves the first n letters to the back of the string

# "Insert {index} {value}":
# Inserts the given value before the given index in the string

# "ChangeAll {substring} {replacement}":
# Changes all occurrences of the given substring with the replacement text
