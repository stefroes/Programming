def kwadraten_som(grondgetallen):
    total = 0

    for getal in grondgetallen:
        if getal > 0:
            total += getal ** 2

    return total


print(kwadraten_som([4, 5, 3, -81]))
