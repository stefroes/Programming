def seizoen(maand):
    maand = int(maand)

    if maand == 12 or maand < 3:
        return 'Winter'
    elif 2 < maand < 6:
        return 'Lente'
    elif 5 < maand < 9:
        return 'Zomer'
    elif 8 < maand < 12:
        return 'Herfst'
    else:
        return False


while True:
    print(seizoen(input('Geef het maand nummer op: ')))
