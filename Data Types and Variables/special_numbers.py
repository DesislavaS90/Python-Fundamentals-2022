number = int(input())

digit_1 = 0
digit_2 = 0
sum_of_digits = 0
for i in range(1, number + 1):
    digit_1 = i % 10
    digit_2 = i // 10
    sum_of_digits = digit_1 + digit_2
    if i == 5 or i == 7:
        print(f'{i} -> True')
    elif sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

