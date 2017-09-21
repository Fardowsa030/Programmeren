# Practice Exercise 6_1 (decision control)

def seizoen(maand):

    if 0 <= maand <= 2:
        print('Het is winter')
    elif 3 <= maand <= 5:
        print('Het is lente')
    elif 6 <= maand <= 8:
        print('Het is zomer')
    elif 9 <= maand <= 11:
        print('Het is herfst')

seizoen(2)

#Practice Exercise 6_2 (lists)

lijst = eval(input('Geef een lijst met minimaal 10 strings: '))
lijst_1 = []
for word in lijst:
    if len(word) == 4:
        lijst_1.append(word)
print(lijst_1)

#Practice Exercise 6_3 (lists)

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
list = str(invoer[0::]).split('-')
for i in range(len(list)):
    list[i] = int(list[i])

for j in range(0,10):
   for k in range(len(list)-1):
       if list[k] > list[k+1]:
          temp = list[k]
          list[k] = list[k+1]
          list[k+1] = temp

gemiddelde = int(sum(list)) / len(list)
print('Gesorteerde list van ints: {}'.format(list))
print('Grootste getal {} en kleinste getal {}'.format(max(list), min(list)))
print('Aantal getallen {} en Som van de getallen {}'.format(len(list), sum(list)))
print('Gemiddelde: {:.2f}'.format(gemiddelde))


# Practice Exercise 6_4 (two-dimensional-lists)


studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
  list = []
  for i in studentencijfers:
      gem = sum(i)/len(i)
      list.append(gem)
  return list

print(gemiddelde_per_student(studentencijfers)) # CHECKEN

def gemiddelde_van_alle_studenten(studentencijfers):
  list = []
  for i in studentencijfers:
      gem = sum(i)/len(i)
      list.append(gem)
  totaal_gemiddelde = sum(list) / len(list)
  return '{:.0f}'.format(totaal_gemiddelde)

print(gemiddelde_van_alle_studenten(studentencijfers))

#Practice Exercise 6_5 (nested loop)

for i in range(1,11): # looping 10 times
    for j in range(1,11):
        print(i * j, end=' ')
    print()



