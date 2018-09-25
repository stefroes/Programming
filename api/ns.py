from private.ns import get_api_login
import requests
import xmltodict


def request(url):
    login = get_api_login()
    try:
        response = requests.get(url, auth=(login['user'], login['password']))
        return xmltodict.parse(response.text)
    except:
        print('Kon geen verbinding maken met de NS API.')


def get_station_details():
    station = input('Over welk station wilt u informatie? ').lower()
    data = request('http://webservices.ns.nl/ns-api-avt?station=' + station)

    print('\nDit zijn de vertrekkende treinen vanaf ' + station.capitalize() + ': ')

    for train in data['ActueleVertrekTijden']['VertrekkendeTrein']:
        time = train['VertrekTijd'][11:16]
        destination = train['EindBestemming']
        sort = train['TreinSoort']
        track = train['VertrekSpoor']['#text']

        print('Om ' + time + ' vertrekt een ' + sort + ' naar ' + destination + ' vanaf spoor ' + track)

    print('\n')


while True:
    get_station_details()
