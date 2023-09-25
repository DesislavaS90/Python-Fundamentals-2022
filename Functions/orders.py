def total_price(my_product: str, product_qty: int):
    if my_product == 'coffee':
        price = 1.50

    elif my_product == 'water':
        price = 1.00

    elif my_product == 'coke':
        price = 1.40

    elif my_product == 'snacks':
        price = 2.00

    return f'{quantity * price:.2f}'


product = input()
quantity = int(input())
print(total_price(product, quantity))