n = int(input())
capacity = 255
counter = 0

for i in range(n):
    liters = int(input())
    if capacity - liters < 0:
        print('Insufficient capacity!')
        continue
    capacity -= liters
    counter += liters
print(counter)
