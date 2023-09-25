password = input()

while True:
    command = input()

    if command == 'Done':
        break

    current_command = command.split()

    if current_command[0] == 'TakeOdd':
        filtered = ''
        for i in range(1, len(password), 2):
            filtered += password[i]
        password = filtered
        print(password)

    elif current_command[0] == 'Cut':
        index = int(current_command[1])
        length = password[index: (index + int(current_command[2]))]
        password = password.replace(length, '', 1)
        print(password)

    elif current_command[0] == 'Substitute':
        substring, substitute = current_command[1], current_command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')


print(f'Your password is: {password}')



# "TakeOdd"
#  Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.

# "Cut {index} {length}"
# Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
# The given index and the length will always be valid.

# "Substitute {substring} {substitute}"
# If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
# If it doesn't, prints "Nothing to replace!".

