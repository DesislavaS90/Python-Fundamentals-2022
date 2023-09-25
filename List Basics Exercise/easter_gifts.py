gifts = input().split()
command = input()

list_command = []
# index_count = []

while command != 'No Money':
    list_command = command.split()

    if list_command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == list_command[1]:
                gifts[i] = 'None'
    elif list_command[0] == 'Required':
        for j in range(len(gifts)):
            if j == int(list_command[2]):
                gifts[j] = list_command[1]
    elif list_command[0] == 'JustInCase':
        gifts[-1] = list_command[1]

    command = input()


for words in gifts:
    if words != 'None':
        print(words, end=' ')
