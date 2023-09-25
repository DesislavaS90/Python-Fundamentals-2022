def min_max_sum(all_numbers):
    list_nums = list(map(int, all_numbers))
    print(f'The minimum number is {min(list_nums)}')
    print(f'The maximum number is {max(list_nums)}')
    print(f'The sum number is: {(sum(list_nums))}')


numbers = input().split()
min_max_sum(numbers)