def urgent_func(item, elements):
    if item not in elements:
        elements.insert(0, item)
    return elements


def unnecessary_func(first_item, elements):
    if first_item in elements:
        elements.remove(first_item)
    return elements


def correct_func(old_item, new_item, elements):
    if old_item in elements:
        for i in range(len(elements)):
            if elements[i] == old_item:
                elements[i] = new_item
    return elements


def rearrange_func(second_item, elements):
    if second_item in elements:
        elements.remove(second_item)
        elements.append(second_item)
    return elements


def grocery_func(elements):

    while True:
        command = input()
        if command == 'Go Shopping!':
            break

        new_command = command.split()
        current_command = new_command[0]

        if current_command == 'Urgent':
            item = new_command[1]
            urgent_func(item, elements)
        elif current_command == 'Unnecessary':
            first_item = new_command[1]
            unnecessary_func(first_item, elements)
        elif current_command == 'Correct':
            old_item = new_command[1]
            new_item = new_command[2]
            correct_func(old_item, new_item, elements)
        elif current_command == 'Rearrange':
            second_item = new_command[1]
            rearrange_func(second_item, elements)
    print(', '.join(elements))


groceries = input().split('!')
grocery_func(groceries)