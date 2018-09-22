unfiltered = eval(input('Geef lijst met minimaal 10 strings: '))
filtered = []

for item in unfiltered:
    if len(item) == 4:
        filtered.append(item)

print('De nieuw-gemaakte lijst met alle vier-letter strings is: \r')
print(filtered)
