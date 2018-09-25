import xmltodict

with open('xml/stations.xml') as file:
    stations = xmltodict.parse(file.read())['Stations']['Station']

    print('Dit zijn de codes en types van de 4 stations:')
    for station in stations:
        print(station['Code'].ljust(4) + ' - ' + station['Type'])

    print('\nDit zijn alle stations met één of meer synoniemen:')
    for station in stations:
            if station['Synoniemen']:
                print(station['Synoniemen'])

    print('\nDit is de lange naam van elk station:')
    for station in stations:
        names = []
        for name in station['Namen']:
            names.append(station['Namen'][name])
        print(station['Code'].ljust(4) + ' - ' + max(names, key=len))
