company = {}

while True:
    command = input()

    if command == 'End':
        break

    name, number = command.split(' -> ')

    if name not in company:
        company[name] = []
    if number not in company[name]:
        company[name] += [number]
for key, value in company.items():
    print(f'{key}')
    for i in value:
        print(f'-- {i}')