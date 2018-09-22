import random


def monopolyworp():
	attempts = 0
	force = False

	while True:
		first = random.randint(1, 6)
		second = random.randint(1, 6)

		result = str(first) + ' + ' + str(second) + ' = ' + str(first + second)

		if first == second:
			attempts = attempts + 1

			if attempts > 2:
				result += ' (direct naar gevangenis)'
				force = True
			else:
				result += ' (dubbel)'
		else:
			force = True

		print(result)

		if force:
			break


monopolyworp()
