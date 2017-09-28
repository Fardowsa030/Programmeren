
naam = input('enter name: ')
while naam != '':
    list = []
    dict = {}
    naam = input('enter name: ')
    list.append(naam)
for item in list:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)
for key in dict:
    if dict[key] == 1:
        print('Er is {} student met de naam {}'.format(dict[key], key))
    else:
            print('Er zijn {} studenten met de naam {}'.format(dict[key], key))
