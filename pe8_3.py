def code(invoerstring):
    coded = ''
    for i in invoerstring:
        coded += chr(ord(i) + 3)

    print(coded)


code('RutteAlkmaarDen Helder')
