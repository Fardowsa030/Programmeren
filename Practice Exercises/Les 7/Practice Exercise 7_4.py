def ticker(filename):
    'geeft dictionary terug'
    dict = {}
    with open(filename, 'r') as bestand:
        regels = bestand.readlines()
    for regel in regels:
        regel = regel.strip('\n')
        regel = regel.split(':')
        dict[regel[0]] = regel[1]
    return dict


companyName = input('Enter Company name: ')

for key, val in ticker('ticker symbols.txt').items():
    if key == companyName:
        print('Ticker symbol: {}'.format(val))

tickerSymbol = input('Enter Ticker symbol: ')

for key, val in ticker('ticker symbols.txt').items():
    if val == tickerSymbol:
        print('Ticker symbol: {}'.format(key))

