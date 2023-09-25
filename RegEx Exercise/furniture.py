import re

text = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
furniture = []
total_price = 0

while text != 'Purchase':
    result = re.search(pattern, text)
    if result:
        item, price, quantity = result.groups()
        furniture.append(item)
        total_price += float(price) * int(quantity)
    text = input()
print('Bought furniture:')
for f in furniture:
    print(f)
print(f'Total money spend: {total_price:.2f}')