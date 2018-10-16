from tkinter import *
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


def get_station_details(event=None):
    station = entry.get().lower()
    data = request('https://webservices.ns.nl/ns-api-avt?station=' + station)

    for widget in frame.winfo_children():
        widget.destroy()

    text = 'Dit zijn de vertrekkende treinen vanaf ' + station.capitalize() + ':'
    Label(master=frame, text=text).pack(pady=5, padx=10)

    for train in data['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
        time = train['VertrekTijd'][11:16]
        destination = train['EindBestemming']
        sort = train['TreinSoort']
        track = train['VertrekSpoor']['#text']

        text = 'Om ' + time + ' vertrekt een ' + sort + ' naar ' + destination + ' vanaf spoor ' + track

        print(text)
        info = Label(master=frame, text=text)
        info.pack(pady=5, padx=10)


root = Tk()
root.bind('<Return>', get_station_details)

frame = LabelFrame(root)
frame.pack(fill='both', expand='yes')

label = Label(master=root, text='Over welk station wilt u informatie?')
label.pack(padx=20, pady=20)

entry = Entry(master=root)
entry.pack(padx=20, pady=20)

button = Button(master=root, command=get_station_details, text='Check reistijden')
button.pack(padx=20, pady=20)


root.mainloop()
