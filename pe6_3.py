invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
numbers = invoer.split('-')
numbers = list(map(int, numbers))
numbers.sort()

print(numbers)
print('Grootste getal: ' + str(max(numbers)) + ' en Kleinste getal: ' + str(min(numbers)) + '\r')
print('Aantal getallen: ' + str(len(numbers)) + ' en Som van de getallen: ' + str(sum(numbers)) + '\r')
print('Gemiddelde: ' + str(sum(numbers) / len(numbers)))
