numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

numbers.sort(reverse=True)
filtered = [num for num in numbers if num > average]
top_five = filtered[:5]

if len(top_five) == 0:
    print('No')
else:
    print(' '.join(map(str, top_five)))