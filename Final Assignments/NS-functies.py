# Deel 1: functie standaardprijs

def standaardprijs(afstandKM):

        if afstandKM < 0:
            afstandKM = 0
        if afstandKM <= 50:
            kosten = afstandKM * 0.80
        else:
            kosten = 15 + afstandKM * 0.60
        return kosten


# Deel 2: functie ritprijs

def ritprijs(leeftijd, weekendrit, afstandKM):

    if weekendrit and leeftijd < 12 or leeftijd > 65:
        korting = standaardprijs(afstandKM) * 0.35
        kosten = standaardprijs(afstandKM) - korting
        return kosten
    elif weekendrit and 12 < leeftijd < 65:
        korting = standaardprijs(afstandKM) * 0.4
        kosten = standaardprijs(afstandKM) - korting
        return kosten
    elif weekendrit == False and leeftijd < 12 or leeftijd > 65:
        korting = standaardprijs(afstandKM) * 0.30
        kosten = standaardprijs(afstandKM) - korting
        return kosten
    elif weekendrit == False and 12 < leeftijd < 65:
        return standaardprijs(afstandKM)

print(ritprijs(50,True,20))








