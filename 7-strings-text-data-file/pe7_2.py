cardnumbers = '../txt/kaartnummers.txt'
file = open(cardnumbers, 'r')

data = []
write = ''

for line in file.readlines():
    data.append(line.split(', '))

for i, people in enumerate(data):
    write += people[1].rstrip() + ' heeft kaartnummer: ' + people[0]
    if i < (len(data) - 1):
        write += '\n'

file = open(cardnumbers, 'w')
file.write(write)

file.close()
