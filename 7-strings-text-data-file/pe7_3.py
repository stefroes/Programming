cardnumbers = '../txt/kaartnummers.txt'
file = open(cardnumbers, 'r')

data = []

for line in file.readlines():
    data.append(line.split(', '))

biggest = max(data)

write = 'Deze file telt ' + str(len(data)) + ' regels \n'
write += 'Het grootste kaartnummer is: ' + biggest[0] + ' en dat staat op regel ' + str(data.index(biggest) + 1)

file = open('txt/kaartnummers.txt', 'w')
file.write(write)

file.close()
