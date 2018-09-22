students = {
	'Henk': 1,
	'Harold': 2,
	'Peter': 3,
	'Willem': 4,
	'Gerard': 5,
	'Jan': 6,
	'Kees': 8,
	'Sam': 9
}

for i, j in students.items():
	if j >= 9:
		print(i + ' heeft een ' + str(j))
