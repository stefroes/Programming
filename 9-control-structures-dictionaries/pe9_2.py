while True:
	word = input('Geef een string van vier letters: ')

	if len(word) == 4:
		print('Inlezen van correcte string: ' + word + ' is geslaagd')
		break
	else:
		print('Fout antwoord: ' + word + ' heeft ' + str(len(word)) + ' letters')
