targets = list(map(int, input().split()))

target_counter = 0
while True:
    command = input()
    if command == 'End':
        break

    index = int(command)

    if index < len(targets):
        number = targets[index]
        targets[index] = -1
        target_counter += 1
        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            elif targets[i] > number:
                targets[i] -= number
            elif targets[i] <= number:
                targets[i] += number
            i += 1
print(f"Shot targets: {target_counter} -> "f"{' '.join(map(str, targets))}")

