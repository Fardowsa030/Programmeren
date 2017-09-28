import csv

with open('artikel.csv', 'r') as file:
    read = csv.DictReader(file,delimiter=';')
    row_prijs = []
    row_naam = []
    row_voorraad = []
    row_artikelnummer = []
    for row in read:
        row['Prijs'] = float(row['Prijs'])
        row_prijs.append(row['Prijs'])
        row_naam.append(row['Naam'])

        row['Voorraad'] = int(row['Voorraad'])
        row_voorraad.append(row['Voorraad'])

        row_artikelnummer.append(row['Artikelnummer'])

    max_prijs = max(row_prijs)
    index_maxprijs = row_prijs.index(max_prijs)
    print('Het duurste artikel is {} en die kost {:.2f} euro'.format(row_naam[index_maxprijs],max_prijs))

    min_voorraad = min(row_voorraad)
    index_minvooraad = row_voorraad.index(min(row_voorraad))
    print('Er zijn slechts {} examplaren in voorraad van het product met de nummer {}'.format(min_voorraad,
                                                                                  row_artikelnummer[index_minvooraad]))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(sum(row_voorraad)))





