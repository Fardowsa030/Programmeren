dict = {}
naam = input('enter name: ')
while naam != '':
    if naam in dict:
       dict[naam] += 1
    else:
        dict[naam] = 1
    naam = input('enter name: ')
for naam,value in dict.items():
    if value == 1:
        print('Er is {} student met de naam {}'.format(value, naam))
    else:
        print('Er zijn {} studenten met de naam {}'.format(value, naam))
