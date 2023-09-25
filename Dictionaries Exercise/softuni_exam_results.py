results = {}
submissions = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    current_command = command.split('-')

    if len(current_command) == 2:
        person = current_command[0]
        del results[person]

    elif len(current_command) == 3:

        if current_command[1] not in submissions:
            submissions[current_command[1]] = 0
        submissions[current_command[1]] += 1

        if current_command[0] not in results:
            results[current_command[0]] = int(current_command[2])
        else:
            if results[current_command[0]] < int(current_command[2]):
                results[current_command[0]] = int(current_command[2])

print('Results:')
for username, points in results.items():
    print(f'{username} | {points}')

print("Submissions:")
for language, submission in submissions.items():
    print(f'{language} - {submission}')