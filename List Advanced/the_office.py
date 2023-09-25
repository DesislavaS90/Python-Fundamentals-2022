employee_happiness = list(map(int, input().split()))
factor = int(input())

multiply = [num * factor for num in employee_happiness]
average = sum(multiply) / len(multiply)
filtered = [employee for employee in multiply if employee > average]

if len(filtered) >= len(employee_happiness) / 2:
    print(f'Score: {len(filtered)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employee_happiness)}. Employees are not happy!')
