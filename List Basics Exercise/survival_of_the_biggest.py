numbers = input().split()
n = int(input())

my_list = []

for i in numbers:
    int_numbers = int(i)
    my_list.append(int_numbers)
for i in range(n):
   my_list.remove(min(my_list))

my_list = map(str, my_list)
print(', '.join(my_list))