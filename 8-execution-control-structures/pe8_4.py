import itertools

studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    antw = []

    for cijfers in studentencijfers:
        antw.append(round(sum(cijfers) / len(cijfers)))

    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    flatten = list(itertools.chain(*studentencijfers))
    antw = round(sum(flatten) / len(flatten))

    return antw


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
