'''
De standaard algebra voorrang regels gelden voor python: * en / hebben voorrang eerder dan + en -,
haakjes worden gebruikt als de volgorde zelf bepaald wordt en als dat allemaal niet lukt fan wordt er \
geoperred van links naar rechts.  // % remainder = 14/3 = 4.666 , 14%3 = 2 , omdat 4.666 *3 == 12, 14- 12 = rest 2
een lijst kan je veranderen(index), string kan je niet een gedeelte verander, moet alles veranderen,tuples niet veranderen
,ordered
'''

# Practice Exercise 1_1 (expressions)   Zie bijlage

# Practice Exercise 1_2 (strings)

# a. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
letters =  'Supercalifragilisticexpialidocious'
print('Er zijn {} letters.'.format(len(letters)))
# b. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
print('ice' in letters)
# c. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
woord_1 = 'Antidisestablishmentarianism'
woord_2 = 'Honorificabilitudinitatibus'
print(len(woord_1) > len(woord_2))
# d. Welke componist komt in alfabetische volgorde het eerst
componist = [ 'Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
componist.sort()
print(componist)

# Practice Exercise 1_3 (statements)

# 1. Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b
a = 6
b = 7
# 2. Ken aan variabele c als waarde het gemiddelde van a en b toe
c = (a + b) / 2
# 3. Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
inventaris = ['papier', 'nietjes', 'pennen']
# 4. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe
voornaam = 'Fardowsa'
tussenvoegsel = ' '
achternaam = 'Hussein'
# 5. Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
mijnnaam = voornaam + tussenvoegsel + achternaam

# Practice Exercise 1_4 (boolean expressions)

# 1. 6.75 groter is dan a en kleiner b
print(6.75 > a and 6.75 < b)
# 2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
print(len(inventaris * 5) > len(mijnnaam))
# 3. de lijst inventaris leeg is, of juist meer dan 10 items bevat.
print(len(inventaris) == 0 or len(inventaris) > 10)

# Practice Exercise 1_5 (lists)

# 1. een nieuwe list met 1 artiest aan te maken met de naam favorieten.
favorieten = ['Beyonce']
# 2. de lijst uit te breiden met een tweede artiest
favorieten.append('Jovi')
# 3. de tweede artiest te vervangen door een andere naam.
favorieten[1] = 'Queens'
print(favorieten)

# Practice Exercise 1_6 (lists)
getallen = [3,7,-2,12]
bereik_getallen = max(getallen) - min(getallen)
print(bereik_getallen)











