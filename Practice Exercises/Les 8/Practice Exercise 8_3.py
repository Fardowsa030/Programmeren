def code(invoercode):
    for letter in invoercode:
        cijfers = ord(letter) + 3
        letters = chr(cijfers)
        print(letters, end='')
code(('RutteAlkmaarDen Helder'))