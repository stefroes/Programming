age = int(input('Geef je leeftijd: '))
passport = input('Nederlands paspoort: ').lower()

if age >= 18 and passport == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
