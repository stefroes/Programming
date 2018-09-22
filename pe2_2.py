cijferICOR = 6
cijferPROG = 9
cijferCSN = 7
price = 30

average = round((cijferICOR + cijferPROG + cijferCSN) / 3, 1)

reward = cijferICOR * price + cijferPROG * price + cijferCSN * price

overview = 'Mijn cijfers (gemiddeld een {}) leveren een beloning van € {} op!'.format(average, reward)

print(overview)
