def namen():
	names = {}

	while True:
		name = input('Volgende naam: ')

		if name != '':
			if name not in names:
				names[name] = 1
			else:
				names[name] = names[name] + 1
		else:
			for i in names:
				if names[i] == 1:
					print('Er is ' + str(names[i]) + ' student met de naam ' + i)
				else:
					print('Er zijn ' + str(names[i]) + ' studenten met de naam ' + i)

			break


namen()
