phonebook = {}

while True:
    entry = input()

    if '-' not in entry:
        break

    name, number = entry.split('-')
    phonebook[name] = number

for person in range(int(entry)):
    contact = input()

    if contact in phonebook:
        print(f'{contact} -> {phonebook[contact]}')

    else:
        print(f'Contact {contact} does not exist.')
