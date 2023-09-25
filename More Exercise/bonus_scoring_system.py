number_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendance_count = 0
max_bonus = 0

while number_students > 0:
    attendance_of_each_student = int(input())
    number_students -= 1
    total_bonus = (attendance_of_each_student / number_of_lectures) * (5 + additional_bonus)
    if total_bonus >= max_bonus:
        max_bonus = 0
        max_bonus += total_bonus
        attendance_count = attendance_of_each_student

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {attendance_count} lectures.')


