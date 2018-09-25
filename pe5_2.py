file = open('txt/kaartnummers.txt', 'r')

data = []
write = ''

for line in file.readlines():
    data.append(line.split(', '))

for i, people in enumerate(data):
    write += people[1].rstrip() + ' heeft kaartnummer: ' + people[0]
    if i < (len(data) - 1):
        write += '\n'

file = open('txt/kaartnummers.txt', 'w')
file.write(write)

file.close()
