# Cette page vise à apprendre les instructions conditionnelles au sein de Python

again = True

if again:
    print('La partie continue !')
else:
    print('C y\'a')

sun = False
snow = True

if sun:
    print("on va à la plage !")
elif snow:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

sunny = True
weekly = False

if sunny and not weekly:
    print("on va à la plage !")
elif sunny and weekly:
    print("on va au travail !")
else:
    print("on reste à la maison !")

un = 1
zero = 0

if un > zero:
    print('yes')
else:
    print('bug :D')
