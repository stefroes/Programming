def convert(celcius):
    return str(celcius * 1.8 + 32).rjust(5)


print('  F       C  ')

for temp in range(-30, 50, 10):
    print('{}   {}'.format(convert(temp), str(temp * 1.0).rjust(5)))
