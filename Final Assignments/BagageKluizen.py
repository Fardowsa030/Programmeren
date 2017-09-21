aantal_kluizen = 12

# keuze menu
menu = int(input('Keuze 1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
                 'Keuze 2: Ik wil een nieuwe kluis\n'
                 'Keuze 3: Ik wil even iets uit mijn kluis halen\n'
                 'Keuze 4: Ik geef mijn kluis terug\n'
                 '\n''Wat is u keuze? : '))


# functie 1
def toon_aantal_kluizen_vrij():
    with open('kluizen.txt', 'r') as data:
        linelist = data.readlines()
        aantal_kluizen_beschikbaar = aantal_kluizen - len(linelist)
    return 'Er zijn {} kluizen op dit moment beschikbaar.'.format(aantal_kluizen_beschikbaar)


# functie 2
def nieuwe_kluizen():
    kluizen_numers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    with open('kluizen.txt', 'r') as data:
        regels = data.readlines()
    for regel in regels:
        regel = regel.strip('\n')  # niet efficient?
        woordlijst = regel.split(';')
        file_nummers = int(woordlijst[0])
        if file_nummers in kluizen_numers:
            kluizen_numers.remove(file_nummers)
        # for i in file_numers:   # gebruik geen for loop maar variable
        # if i in kluizen_numers:
        # kluizen_numers.remove(i)
    if len(kluizen_numers) > 0:
        wachtwoord = input('Enter u paswoord: ')
        if len(wachtwoord) > 2:
            with open('kluizen.txt', 'a') as data:
                data.write('{};{}\n'.format(kluizen_numers[0], wachtwoord))
                return 'U krijgt kluisnummer {}'.format(kluizen_numers[0])
        else:
            return 'Een wachtwoord moet uit meer dan 2 letters bestaan.'
    else:
        return 'Er zijn nu geen kluizen beschikbaar, probeer het op een later tijdstip!'


# functie 3

def kluis_openen():
    ''
    kluisnummer = int(input('Wat is u kluisnummer: '))
    kluiscode = input('Wat is u kluiscode: ')
    with open('kluizen.txt', 'r') as kluizen_bestand:
        regels = kluizen_bestand.readlines()
    for regel in regels:
        regel = regel.strip('\n')
        woordlijst = regel.split(';')
        filenummers = int(woordlijst[0])
        if kluisnummer == filenummers and kluiscode == woordlijst[1]:
           return 'De kluis is open '
    return 'De kluis is niet open probeer het opnieuw'



if menu == 1:
    print(toon_aantal_kluizen_vrij())
elif menu == 2:
    print(nieuwe_kluizen())
elif menu == 3:
    print(kluis_openen())