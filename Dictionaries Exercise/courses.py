courses = {}

while True:
    command = input()

    if command == 'end':
        break

    course, name = command.split(' : ')

    if course not in courses:
        courses[course] = []
    courses[course] += [name]


for course_name, student_name in courses.items():
    print(f'{course_name}: {len(student_name)}')
    for i in student_name:
        print(f"-- {i}")
