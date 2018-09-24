import csv

with open('Games.csv') as file:
    reader = csv.reader(file, delimiter=';')
    scores = []

    for row in reader:
        row[2] = int(row[2])
        scores.append(row)

    highest = max(scores, key=lambda x: x[2])

    print('De hoogste score is: ' + str(highest[2]) + ' op ' + highest[1] + ' behaald door ' + highest[0])
