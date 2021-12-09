print('Test sur la boucle for')
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(5):
    print(x)

for x in range(6): # f en début de print permet de définir un format
    print(f"{x} bouteilles de bières au mur !")

try:
    for x in range(6): # sans le f + {} pour cibler, on aurait une erreur
        print(x+" bouteilles de bières au mur !")
except TypeError:
    print('/!\\ Il faut cast sinon on a une erreur')
finally:
    print('Cette partie sera executée qu\'on passe dans le try ou l\'except')

print('Test sur la boucle while')
capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    print(f'Plus que {capacite_maximale-capacite_actuelle} dans la boucle while')
    capacite_actuelle += 1

if capacite_actuelle == capacite_maximale:
    print('Capacite maximale atteinte')
