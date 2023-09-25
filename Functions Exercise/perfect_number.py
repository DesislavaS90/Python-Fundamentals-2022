def perfect_number(n):
    number_sum = 0

    for i in range(1, n):
        if n % i == 0:
            number_sum += i
    if number_sum == n:
        return 'We have a perfect number!'

    return 'It\'s not so perfect.'


number = int(input())
print(perfect_number(number))