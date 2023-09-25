sequence = input().split()
command = input()

moves = 0

while command != 'end':
    moves += 1
    index1 = int(command.split()[0])
    index2 = int(command.split()[1])

    if index1 == index2 or index1 < 0 or index2 < 0 or\
       index1 >= len(sequence) or index2 >= len(sequence):
        sequence.insert(int(len(sequence) / 2), f"-{str(moves)}a")
        sequence.insert(int(len(sequence) / 2), f"-{str(moves)}a")
        print('Invalid input! Adding additional elements to the board')

    elif sequence[index1] == sequence[index2]:
        print(f'Congrats! You have found matching elements - {sequence[index1]}!')

        i = sequence.pop(index1)
        sequence.remove(i)

    elif sequence[index1] != sequence[index2]:
        print('Try again!')

    if len(sequence) == 0:
        print(f'You have won in {moves} turns!')
        break

    command = input()
if command == 'end':
    print("Sorry you lose :(\n" f"{' '.join(sequence)}")
