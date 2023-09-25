orders = int(input())

total = 0

for i in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31\
            or capsules_needed < 1 or capsules_needed > 2000:

        continue

    total_price_coffee = price_per_capsule * days * capsules_needed
    total += total_price_coffee

    print(f'The price for the coffee is: ${total_price_coffee:.2f}')


print(f'Total: ${total:.2f}')

