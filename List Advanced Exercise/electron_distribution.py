number_of_electrons = int(input())

shells_list = []

counter = 0

while number_of_electrons > 0:
    counter += 1

    shell = 2 * counter ** 2

    if number_of_electrons >= shell:
        shells_list.append(shell)
        number_of_electrons -= shell
    else:
        shells_list.append(number_of_electrons)
        number_of_electrons = 0
print(shells_list)
