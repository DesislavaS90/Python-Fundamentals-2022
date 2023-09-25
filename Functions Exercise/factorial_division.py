def factorial(a, b):
    sum_a = 1
    sum_b = 1
    for i in range(1, a + 1):
        sum_a *= i
    for k in range(1, b + 1):
        sum_b *= k
    return f'{sum_a / sum_b:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))