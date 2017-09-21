while True:
    zin = input('Geef een string van vier letters: ')
    if len(zin) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(zin))
        break
    else:
        print('{} heeft {} letters'.format(zin,len(zin)))

