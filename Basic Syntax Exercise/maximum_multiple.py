divisor = int(input())
boundary = int(input())

number = 0

for i in range(divisor, boundary + 1):
    if i > 0:
        if i % divisor == 0 and i <= boundary:
            number = i
print(number)
