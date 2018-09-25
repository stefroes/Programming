stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


def valid_station(station):
    if station in stations:
        return station
    else:
        print('Deze trein komt niet in ' + station)
        return False


def inlezen_beginstation():
    while True:
        station = input('Wat is je beginstation? ')
        if valid_station(station):
            return station


def inlezen_eindstation(beginstation):
    while True:
        eindstation = input('Wat is je eindstation? ')
        if valid_station(eindstation):
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            else:
                print('Uw eindstation moet verder zijn dan uw beginstation.')


def omroepen_reis(beginstation, eindstation):
    begin_index = stations.index(beginstation)
    end_index = stations.index(eindstation)
    diff = stations.index(eindstation) - stations.index(beginstation)

    print('\nHet beginstation ' + beginstation + ' is het ' + str(begin_index + 1) + 'e station in het traject.')
    print('Het eindstation ' + eindstation + ' is het ' + str(end_index + 1) + 'e station in het traject.')
    print('De afstand bedraagt ' + str(diff) + ' station(s).')
    print('De prijs van het kaartje is ' + str(diff * 5) + ' euro.')

    print('\nJij stapt in de trein in: ' + beginstation)
    for station in stations[begin_index + 1:end_index]:
        print('- ' + station)
    print('Jij stapt uit in: ' + eindstation)


start = inlezen_beginstation()
end = inlezen_eindstation(start)
omroepen_reis(start, end)
