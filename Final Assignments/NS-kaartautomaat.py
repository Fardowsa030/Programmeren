stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'AmsterdamCentraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']


while True:
    begin_station = input('Wat is u beginstation: ')
    if begin_station in stations:
        break

while True:
    eind_station = input('Wat is u eindstation: ')
    if eind_station in stations and stations.index(eind_station) >= stations.index(begin_station):
        break

print('Het beginstation {} is het {} station in het traject'.format(begin_station,stations.index(begin_station)+1))
print('Het eindstation {} is het {} station in het traject'.format(eind_station,stations.index(eind_station)+1))
index_beginstation = stations.index(begin_station)+1
index_eindstation = stations.index(eind_station) +1
verschil = index_eindstation - index_beginstation
prijs = verschil * 5
print('de afstand bedraagt {} station(s)'.format(verschil))
print('de prijs van het kaartje is {}'.format(prijs))
