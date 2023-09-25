def even_numbers(number):
    int_list = []
    for i in number:
        if int(i) % 2 == 0:
            int_list.append(int(i))
    return int_list


numbers = input().split()
print(even_numbers(numbers))
