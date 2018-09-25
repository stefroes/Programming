def ticker(filename):
	file = open(filename)
	data = {}

	for company in file.read().splitlines():
		splited = company.split(':')
		data[splited[0]] = splited[1]

	return data


def get_ticker_by_company():
	companies = ticker('txt/ticker.txt')
	name = input('Enter Company name: ')
	print('Ticker symbol: ' + companies.get(name) + '\n')


def get_company_by_ticker():
	companies = ticker('txt/ticker.txt')
	tick = input('Enter Ticker symbol: ')

	for i in companies:
		if companies[i] == tick:
			print('Company name: ' + i + '\n')
			break


get_ticker_by_company()
get_company_by_ticker()
