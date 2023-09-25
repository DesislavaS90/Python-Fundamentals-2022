messages = int(input())

for i in range(messages):
    type_message = int(input())
    if type_message == 88:
        print('Hello')
    elif type_message == 86:
        print('How are you?')
    elif type_message > 88:
        print('Bye.')
    else:
        print('GREAT!')
