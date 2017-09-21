# Practice Exercise 3_1 (if-statement)

score = int(input('Geef je score: '))

if score > 15:
    print('Met een score van {} ben je geslaagd '.format(score))
else:
    print('Je bent niet geslaagd')

# Practice Exercise 3_2 (if met 2 booleaanse operators) + Practice Exercise 3_3 (if-else)

leeftijd = int(input('Geef je leeftijd: '))
paspoort = input('Heeft u een nederlandse paspoort (ja/nee): ')

if leeftijd >= 18 and paspoort.lower() == 'ja':
    print('Gefeliciteerd je mag stemmen!')
else:
    print('Je mag niet stemmen')

# Practice Exercise 3_4 (for + if)

dagen = ['maandag', 'woensdag', 'donderdag']
for i in dagen:
    print(i[:2], end=' ')
print()

# Practice Exercise 3_5 (for + if)

for i in range(1, 21):
    if (i % 2) == 0:
        print(i, end=' ')
print()

# Practice Exercise 3_6 (for + if)

s = "Guido van Rossum"
for i in s:
    if i in 'aeiouAEIOU':
        print(i, end=' ')