students = {}

while True:
    command = input()

    if ':' not in command:
        break

    current_command = command.split(':')
    course, student, number = current_command[2], current_command[0], current_command[1]

    if course in students:
        students[course] += [f'{student} - {number}']
    else:
        students[course] = [f'{student} - {number}']

wanted_course = command.replace('_', ' ')
print('\n'.join(students[''.join(wanted_course)]))


