def sorting_names(elements):
    return sorted(elements, key=lambda name: (-len(name), name))


names = list(input().split(', '))
print(sorting_names(names))
