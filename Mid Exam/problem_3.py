book_shelf = input().split('&')

while True:
    command = input()
    if command == 'Done':
        break
    current_command = command.split(' | ')

    if current_command[0] == 'Add Book':
        if current_command[1] not in book_shelf:
            book_shelf.insert(0, current_command[1])

    elif current_command[0] == 'Take Book':
        if current_command[1] in book_shelf:
            book_shelf.remove(current_command[1])

    elif current_command[0] == 'Swap Books':
        first_book = current_command[1]
        second_book = current_command[2]
        if first_book in book_shelf and second_book in book_shelf:
            first_index = book_shelf.index(first_book)
            second_index = book_shelf.index(second_book)
            book_shelf[first_index], book_shelf[second_index] = book_shelf[second_index], book_shelf[first_index]

    elif current_command[0] == 'Insert Book':
        book = current_command[1]
        if book not in book_shelf:
            book_shelf.append(book)

    elif current_command[0] == 'Check Book':
        index = int(current_command[1])
        if index <= len(book_shelf):
            print(book_shelf[index])

print(', '.join(book_shelf))