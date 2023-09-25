import functools
orders = {}

while True:
    command = input()

    if command == 'buy':
        break

    name, price, quantity = command.split()

    if name not in orders:
        orders[name] = [float(price), int(quantity)]
    else:
        orders[name][1] += int(quantity)
        orders[name][0] = float(price)

for product_name, total_price in orders.items():
    total_price = functools.reduce((lambda x, y: x * y), total_price)
    print(f'{product_name} -> {total_price:.2f}')