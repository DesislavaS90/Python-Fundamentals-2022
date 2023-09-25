first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())

students_per_hour = first_employee + second_employee + third_employee
time = 0

while number_of_students > 0:

    number_of_students -= students_per_hour
    time += 1

    if time % 4 == 0:
        time += 1

print(f'Time needed: {time}h.')