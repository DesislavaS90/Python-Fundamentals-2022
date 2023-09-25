some_string = input().split()

result = 0

for string in some_string:
    num = int(string[1:len(string) - 1])
    first = string[0]
    second = string[-1]
    if first.isupper():
        result += num / abs(ord(first) - 64)
    elif first.islower():
        result += num * abs(ord(first) - 96)

    if second.isupper():
        result -= ord(second) - 64
    elif second.islower():
        result += ord(second) - 96


print(f'{result:.2f}')