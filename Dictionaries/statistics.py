bakery = {}

while True:
    command = input()

    if command == 'statistics':
        break

    key, value = command.split(': ')

    if key not in bakery:
        bakery[key] = int(value)
    else:
        bakery[key] += int(value)

print(f'Products in stock:')

for (key, value) in bakery.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(bakery)}')
print(f'Total Quantity: {sum(bakery.values())}')
