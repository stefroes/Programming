lockers = []
total = 12
used = []
filename = '../txt/kluizen.txt'


def refresh_locker_data():
	file = open(filename)
	data = file.readlines()
	file.close()

	global lockers
	global used

	lockers = []
	used = []

	for locker in data:
		locker = locker.split(';')
		locker[0] = int(locker[0])
		locker[1] = locker[1].replace('\n', '')
		lockers.append(locker)
		used.append(locker[0])


def has_free_locker():
	return total - len(lockers) >= 1


def toon_aantal_kluizen_vrij():
	if has_free_locker():
		print('Er zijn ' + str(total - len(lockers)) + ' kluizen beschikbaar')
	else:
		print('Er is geen locker beschikbaar')


def nieuwe_kluis():
	options = list(range(1, total + 1))
	ordered_lockers = sorted(lockers)

	for locker in ordered_lockers:
		if locker[0] in options:
			options.pop(options.index(locker[0]))

	password = input('Voer uw wachtwoord voor een kluis in: ')

	while '\n' in password:
		print('De karakters: "\\n" mogen niet voorkomen in uw wachtwoord')

	write = '\n' + str(options[0]) + ';' + password

	append = open(filename, 'a')
	if append.write(write):
		print('U heeft kluis: ' + str(options[0]) + '. Ontgrendel deze met uw wachtwoord.\n')
	append.close()


def kluis_openen():
	nummer = int(input('Geef uw kluisnummer op: '))
	wachtwoord = input('Geef uw wachtwoord op: ')

	found = False

	for locker in lockers:
		if locker[0] == nummer and locker[1] == wachtwoord:
			found = True
			print('Uw kluis ' + str(locker[0]) + ' is open')

	if not found:
		print('Kluisnummer of wachtwoord is niet correct')


def kluis_teruggeven():
	nummer = int(input('Geef uw kluisnummer op: '))
	wachtwoord = input('Geef uw wachtwoord op: ')

	found = False

	for locker in lockers:
		if locker[0] == nummer and locker[1] == wachtwoord:
			found = True
			write = ''

			lockers.remove(locker)

			for index, locker in enumerate(lockers):
				write += str(locker[0]) + ';' + locker[1]

				if locker != lockers[-1]:
					write += '\r'

			append = open(filename, 'w')
			if append.write(write):
				print('Uw kluis ' + str(locker[0]) + ' is vrijgegeven')
			break

	if not found:
		print('Kluisnummer of wachtwoord is niet correct')


while True:
	refresh_locker_data()
	print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
	print('2: Ik wil een nieuwe kluis')
	print('3: Ik wil even iets uit mijn kluis halen')
	print('4: Ik geef mijn kluis terug')
	print('5: Ik wil stoppen\n')

	option = int(input('Kies uit optie 1, 2, 3, 4 of 5: '))

	if option == 1:
		toon_aantal_kluizen_vrij()
	elif option == 2:
		if has_free_locker():
			nieuwe_kluis()
		else:
			print('Er is geen locker beschikbaar')
	elif option == 3:
		kluis_openen()
	elif option == 4:
		kluis_teruggeven()
	elif option == 5:
		break
	else:
		print('Geen geldige invoer')

	print('\n-----------------\n')
