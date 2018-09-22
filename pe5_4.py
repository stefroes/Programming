import datetime


def get_time():
    return datetime.datetime.today().strftime("%a %d %b %Y, %H:%M:%S")


file = open('Hardlopers.txt', 'a')

while True:
    name = input('Voer naam van de harloper in: ')
    if name == '':
        break
    runner = get_time() + ', ' + name + '\n'
    file.write(runner)
