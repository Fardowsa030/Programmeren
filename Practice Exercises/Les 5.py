# Practice Exercise 5_1 (formatting)

def convert(Celcius):
    fahr = Celcius * 1.8 + 32
    return fahr

print(convert(25))
print()

def table():
    for i in range(-30,50,10):
        fahr = i * 1.8 + 32
        print('{0:4} {1:9}'.format(i,fahr))
table()
print()

#Practice Exercise 5_2 (files lezen)

with open('kaartnummers.txt', 'r') as bestand:
    regels = bestand.readlines()
for regel in regels:
    lijst = regel.split(',')
    woord = 'heeft kaartnummer:'
    lijst_2 ='{} {} {}'.format(lijst[1].strip('\n'),woord,lijst[0])
    print(lijst_2)
print()
# Practice Exercise 5_3 (files lezen)

list_nummers = []
with open('kaartnummers.txt', 'r') as bestand:
    regels = bestand.readlines()
for regel in regels:
    regel = regel.strip('\n')
    lijst = regel.split(',')
    nummers = int(lijst[0])
    list_nummers.append(nummers)

print('Deze file telt {} regels.'.format(len(regels)))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(max(list_nummers),list_nummers.index(max(list_nummers))+1))
# regel vinden? index start 0

# Practice Exercise 5_4 (files schrijven)

import time
datum = time.strftime('%a %d %B %Y')
tijd = time.strftime('%I:%M:%S')
#naam = input('Wat is u naam? :')
#with open('hardlopers.txt', 'a') as bestand:
    #bestand.write('{}, {}, {}\n'.format(datum,tijd,naam))

# Practice Exercise 5_5 (string functions)

def gemiddelde():

    zin = input('Geef een willekeurige zin: ').split()
    for woord in zin:
        lengte_woord = len(woord)
        aantal_woorden = len(zin)
        gemiddelde_lengte = lengte_woord / aantal_woorden
        print('De gemiddelde lengte van het woord is: {}'.format(gemiddelde_lengte))

gemiddelde() # vragen over de vraag betekenis en of klopt (stackoverflow)
