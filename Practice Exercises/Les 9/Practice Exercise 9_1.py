try:
  aantal_personen = int(input('Hoeveel personen reizen mee: '))
  kosten = 4356
  delen = kosten / aantal_personen
  if aantal_personen < 0:
      raise Exception
  print(delen)
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except ValueError:
    print('Alleen nummers invoeren!')
except Exception:
    print('Geen negatieve getallen!')
except:
    print('andere errors')

