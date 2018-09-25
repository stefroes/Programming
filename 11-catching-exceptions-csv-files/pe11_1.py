def calculate_person_price(persons):
    try:
        persons = int(persons)
        if persons < 0:
            raise ValueError

        amount = 4356 / persons
        print('Per persoon kost dit € ' + str(amount))
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Negatieve getallen zijn niet toegestaan!')
    except TypeError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except:
        print('Onjuiste invoer!')


while True:
    calculate_person_price(input('Aantal personen: '))
