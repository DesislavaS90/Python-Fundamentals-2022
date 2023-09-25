n = int(input())

negative = []
positive = []

for i in range(n):
    numbers = int(input())
    if numbers < 0:
        negative.append(numbers)
    if numbers >= 0:
        positive.append(numbers)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')