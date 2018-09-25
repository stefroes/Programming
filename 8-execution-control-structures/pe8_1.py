def seizoen(maand):
    maand = int(maand)

    if 3 >= maand >= 1:
        return 'Winter'
    elif 6 >= maand >= 4:
        return 'Lente'
    elif 9 >= maand >= 7:
        return 'Zomer'
    elif 12 >= maand >= 10:
        return 'Herfst'
    else:
        return False


print(seizoen(input('Geef het maand nummer op: ')))
