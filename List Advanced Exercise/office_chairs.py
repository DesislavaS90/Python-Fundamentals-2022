def room_check(rooms_number):
    chairs_need = 0
    free_chairs = 0
    for room in range(1, rooms_number + 1):
        chairs, rooms = input().split()
        diff = len(chairs) - int(rooms)
        if diff >= 0:
            free_chairs += diff
        else:
            chairs_need += abs(diff)
            print(f'{abs(diff)} more chairs needed in room {room}')
    return chairs_need, free_chairs


number_of_rooms = int(input())
needed, free = room_check(number_of_rooms)

if free >= needed:
    print(f'Game On, {free} free chairs left')