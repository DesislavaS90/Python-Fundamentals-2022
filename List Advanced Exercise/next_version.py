version = [int(number) for number in input().split('.')]

version[-1] += 1

for i in range(len(version) - 1, -1, -1):
    if version[i] > 9:
        version[i] = 0
        if i - 1 >= 0:
            version[i - 1] += 1

print('.'.join(map(str, version)))




