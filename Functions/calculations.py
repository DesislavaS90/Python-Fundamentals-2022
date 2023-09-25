def operator_func(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


type_operator = input()
number_a = int(input())
number_b = int(input())

print(operator_func(type_operator, number_a, number_b))
