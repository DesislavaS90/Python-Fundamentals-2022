number = int(input())

for i in range(0, number):
    for m in range(0, number):
        for n in range(0, number):
            print(f'{chr(97 + i)}{chr(97 + m)}{chr(97 + n)}')