
price_without_taxes = 0
taxes = 0
final_price = 0

command = input()
while command != 'special' and command != 'regular':

    price = float(command)

    if price < 0:
        print('Invalid price!')

    else:
        price_without_taxes += price
        taxes += price * 0.2

    command = input()

total_price = taxes + price_without_taxes

if command == 'special':
    final_price = total_price - (total_price * 0.1)

else:
    final_price = total_price


if total_price == 0:
    print('Invalid order!')

else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_taxes:.2f}$\n\
Taxes: {taxes:.2f}$\n-----------\nTotal price: {final_price:.2f}$")








