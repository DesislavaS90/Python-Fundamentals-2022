def sorted_numbers(all_numbers):
    return sorted(list(map(int, all_numbers)))


numbers = input().split()
print(sorted_numbers(numbers))