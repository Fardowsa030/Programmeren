import time
import csv

with open('gegevens.csv', 'w',newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=':')
    writer.writerow(('datum','naam','voorletters','geboortedatum','email'))
    datum = time.strftime('%a %d %B %Y  %I:%M:%S')
    while True:
       naam = input('Wat is je achternaam? ')
       if naam == 'einde':
         break
       voorletters = input('Wat zijn je voorletters? ')
       geboortedatum = input('Wat is u geboortedatum? ')
       email = input('Wat is u email? ')
       writer.writerow((datum, naam,voorletters,geboortedatum,email))




