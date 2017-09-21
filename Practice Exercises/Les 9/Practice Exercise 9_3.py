import csv

with open('gamers.csv', 'r',newline='') as myFile:
    read = csv.reader(myFile, delimiter=';')
    list_naam = []
    list_datum = []
    list_score = []
    for row in read:
        print(type(row))
        list_naam.append(row[0])
        list_datum.append(row[1])
        list_score.append(row[2])
    print('De hoogste score: {} op {} behaal door {}'.format(list_score[-1],list_datum[-1],list_naam[-1]))








