# Practice Exercise 4_1 (functie met 3 parameters)

def som(getal1,getal2,getal3):
    getallen = [getal1,getal2,getal3]
    return sum(getallen)
print(som(1,2,3))

# Practice Exercise 4_2 (functie met list-parameter)

def som(getallenlijst):
    return sum(getallenlijst)
print(som([2,4,6,8]))

# Practice Exercise 4_3 (functie met if)

def lang_genoeg(lengte):
    if lengte >= 120:
        return 'Je bent lang genoeg voor de attractie'

    return 'Sorry je bent te klein'
print(lang_genoeg(130))

# Practice Exercise 4_4 (functie met if)

def new_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return True
    return False
print(new_password('Game of Thrones','Narcos'))

# Practice Exercise 4_5 (functie met list-parameter en for-loop)

def kwadraten_som(grondgetallen):
    lijst = []
    for getal in grondgetallen:
        if getal <= 0:
            getal = 0
        lijst.append(getal ** 2)
    return sum(lijst)

print(kwadraten_som([2,4,-52]))


# Practice Exercise 4_6 (functie met (im)mutable parameter)

def wijzig(letterlijst):
    letters = ['d', 'e', 'f']
    print(letterlijst)
    letterlijst.clear()
    for i in letters:
      letterlijst.append(i)
    print(letterlijst)

wijzig(['a','b','c'])