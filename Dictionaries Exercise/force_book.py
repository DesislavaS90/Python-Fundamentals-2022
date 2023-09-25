force_book = {}

while True:

    command = input()

    if command == 'Lumpawaroo':
        break

    if '|' in command:
        side, user = command.split(' | ')
        if side not in force_book:
            force_book[side] = []
        if [user] in force_book.values():
            continue
        else:
            force_book[side] += [user]

    elif '->' in command:
        user1, side1 = command.split(' -> ')
        if side1 not in force_book:
            force_book[side1] = []
        if [user1] not in force_book.values():
            force_book[side1] += [user1]
        else:
            for key, value in force_book.items():
                if user1 in force_book[key]:
                    del force_book[key]
                    force_book[side1] += [user1]
                    break
        print(f'{user1} joins the {side1} side!')

for key, value in force_book.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(force_book[key])}')
    for i in value:
        print(f'! {i}')





