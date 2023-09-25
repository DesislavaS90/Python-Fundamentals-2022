elements = input().split()
bakery = {}
for element in range(0, len(elements), 2):
    bakery[elements[element]] = int(elements[element + 1])
print(bakery)