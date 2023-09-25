level_of_fire = input().split('#')
amount_of_water = int(input())

effort = 0
total_fire = 0
cell = []

for level in level_of_fire:
    level = level.split('=')
    water_needed = int(level[1])
    if level[0] == 'High ' and 81 <= water_needed <= 125 and amount_of_water >= water_needed:
        cell.append(water_needed)
        amount_of_water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed
    elif level[0] == 'Medium ' and 51 <= water_needed <= 80 and amount_of_water >= water_needed:
        cell.append(water_needed)
        amount_of_water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed
    elif level[0] == 'Low ' and 1 <= water_needed <= 50 and amount_of_water >= water_needed:
        cell.append(water_needed)
        amount_of_water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed

print('Cells:')
for i in range(len(cell)):
    print(f' - {cell[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')