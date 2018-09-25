def standaardprijs(afstand_km):
    if afstand_km <= 0:
        return 0
    elif afstand_km <= 50:
        return .8 * afstand_km
    else:
        return .6 * afstand_km + 15


def ritprijs(leeftijd, weekendrit, afstand_km):
    discount = 1
    if leeftijd < 12 or leeftijd >= 65:
        discount -= .3
        if weekendrit:
            discount -= .05
    elif weekendrit:
        discount -= .4

    if discount < 0:
        discount = 0

    return round(discount * standaardprijs(afstand_km), 2)
