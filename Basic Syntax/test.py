orders = int(input())

total = 0

for i in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if 0.01 > price_per_capsule < 100.00 or 1 > days < 31 or 1 < capsules_needed < 2000:
        continue

    total_price_coffee = price_per_capsule * days * capsules_needed

    print(f'The price for the coffee is: ${total_price_coffee:.2f}')

    total += total_price_coffee

print(f'Total: ${total:.2f}')