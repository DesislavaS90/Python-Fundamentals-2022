def even_index(elements):
    even_list = [i for i, e in enumerate(elements) if e % 2 == 0]
    return even_list


numbers = list(map(int, input().split(', ')))
print(even_index(numbers))