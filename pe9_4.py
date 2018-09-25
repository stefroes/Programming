import csv

with open('csv/products.csv') as file:
    reader = csv.reader(file, delimiter=';')
    products = []
    total = 0

    next(reader, None)

    for row in reader:
        row[0] = int(row[0])
        row[3] = int(row[3])
        row[4] = float(row[4])
        total += row[3]
        products.append(row)

    expensivest = max(products, key=lambda x: x[4])
    stock = min(products, key=lambda x: x[3])

    print('Het duurste artikel is ' + expensivest[2] + ' en die kost ' + str(expensivest[4]) + ' Euro')
    print('Er zijn slechts ' + str(stock[3]) + ' exemplaren in voorraad van het product met nummer ' + str(stock[0]))
    print('In totaal hebben wij ' + str(total) + ' producten in ons magazijn liggen')
