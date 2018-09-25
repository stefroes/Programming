import csv
import datetime

bestand = 'csv/inloggers.csv'

with open(bestand, 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(('Datum', 'Naam', 'Voorletters', 'Geboortedatum', 'E-mail'))

    while True:
        naam = input('Wat is je achternaam? ')
        if naam == 'einde':
            break
        voorletters = input('Wat zijn je voorletters? ')
        geboortedatum = input('Wat is je geboortedatum? ')
        email = input('Wat is je e-mail adres? ')
        print('\r')

        writer.writerow((datetime.datetime.now(), naam, voorletters, geboortedatum, email))
