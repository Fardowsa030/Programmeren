list = []
while True:
    getal = int(input('Geef een getal: '))
    if getal == 0:
        break
    else:
        list.append(getal)
if len(list) == 1:
  print('Er is {} getal ingevoerd, de som is: {}'.format(len(list),sum(list)))
else:
    print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(list),sum(list)))

