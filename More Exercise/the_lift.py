people = int(input())
current_state = input().split()

wagon_list = []

for wagon in map(int, current_state):

    if wagon >= 0:
        people += wagon

    if people >= 4:
        wagon_list.append(4)
        people -= 4
    elif people < 4:
        wagon_list.append(people)
        people -= people

if wagon_list[-1] < 4:
    print(f"The lift has empty spots!")

elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(' '.join(map(str, wagon_list)))




