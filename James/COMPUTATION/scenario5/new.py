student_grades = [57, 74, 49, 0, 87, 66, 89]

for g in student_grades:
	assert student_grades[g] != 0
	if student_grades[g] >= 52:
		print('This student passed.')
	else:
		print('This student failed.')

print('Program complete')