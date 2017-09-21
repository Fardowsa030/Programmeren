# Practice Exercise 2_1 (tuples)

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
lijst = [letters.count('A'),letters.count('B'), letters.count('C')]
print(lijst)

# Practice Exercise 2_2 (getallen, strings en conversie)

cijferICOR = 7
cijferPROG = 8
cijferCSN = 7
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning =  (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een {:.1f}) leveren een beloning van € {} op!'.format(gemiddelde,beloning)
print(overzicht)

# Practice Exercise 2_3 (operator voorrang) # false = 0 , true = 1

# 1.   0 == 1 == 2
print(0 == (1==2))
# 2.   2 + 3 == 4 + 5 == 7
print(2+(3==4)+5==7)
# 3.   1 < -1 == 3 > 4
print((1< -1) == (3 > 4))


# Practice Exercise 2_4 (Input/Output)

uurloon = eval(input('Wat is u uurloon: '))
aantal_uur = eval(input('Hoeveel uur heeft u gewerkt: '))
salaris = uurloon * aantal_uur
print('{} uur werken levert {} Euro op'.format(aantal_uur,salaris))
