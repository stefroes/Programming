def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0
    elif afstandKM <= 50:
        return .8 * afstandKM
    else:
        return .6 * afstandKM + 15


def ritprijs(leeftijd, weekendrit, afstandKM):
    discount = 1
    if leeftijd < 12 or leeftijd >= 65:
        discount -= .3
        if weekendrit:
            discount -= .05
    elif weekendrit:
        discount -= .4

    if discount < 0:
        discount = 0

    return round(discount * standaardprijs(afstandKM), 2)
