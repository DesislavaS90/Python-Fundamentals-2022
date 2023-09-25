bakery = input().split(' ')
elements = input().split()

my_dict = {}

for product in range(0, len(bakery), 2):
    key = bakery[product]
    value = int(bakery[product + 1])
    my_dict[key] = value

for element in elements:
    if element in bakery:
        print(f'We have {my_dict[element]} of {element} left')
    else:
        print(f'Sorry, we don\'t have {element}')