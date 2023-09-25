numbers = list(map(int, input().split(', ')))

group = 10
nums = []

while len(numbers) > 0:

    for num in numbers:
        if num <= group:
            nums.append(num)

    for i in nums:
        numbers.remove(i)

    print(f'Group of {group}\'s: {nums}')

    group += 10
    nums = []
