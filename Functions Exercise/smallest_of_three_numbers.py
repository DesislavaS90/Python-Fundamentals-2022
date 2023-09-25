def the_smallest_number(numbers):
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
min_number = [first_number, second_number, third_number]
total = the_smallest_number(min_number)
print(total)