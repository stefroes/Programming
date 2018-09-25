money = input('Wat verdien je per uur?')
hour = input('Hoeveel uur heb je gewerkt')
earned = int(hour) * float(money)

print('{} uur werken levert {} Euro op'.format(hour, earned))
