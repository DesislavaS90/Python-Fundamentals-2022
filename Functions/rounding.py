def rounding(numbers):
    list = []
    for n in numbers:
        list.append(round(float(n)))
    return list


number = input().split()
print(rounding(number))