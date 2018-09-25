numbers = []

while True:
	number = int(input('Geef een getal: '))

	if number != 0:
		numbers.append(number)
	else:
		print('Er zijn ' + str(len(numbers)) + ' getallen ingevoerd, de som is: ' + str(sum(numbers)))
		break
