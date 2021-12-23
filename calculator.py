play = True


def calc(a, s, b):
    if s == '-':
        result = a - b
    elif s == '+':
        result = a + b
    elif s == '/':
        result = a / b
    elif s == '*':
        result = a * b
    else:
        result = ' C\'est quoi ce signe ? -_-'
    return result


def game(p):
    a = int(input('Saisissez une valeur :    '))
    signe = input('Saisissez un signe (+, -, /, *) :     ')
    b = int(input('Saisissez une autre valeur :     '))
    print(calc(a, signe, b))
    again = input('Voulez-vous continuer ? Oui appuyez sur une touche sinon 0')
    if again == '0':
        p = False
    return p


while play:
    play = game(play)
