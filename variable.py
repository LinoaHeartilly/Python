# déclaration variable
livre = "Harry Potter"

# Affichage dans la console
print(livre)

livre = livre + " 2"
print(livre)

# liste
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print(plateformes_sociales[0])
# Ajout puis remove dans liste
plateformes_sociales.append('TikTok')
print(plateformes_sociales)
print(plateformes_sociales[4])
plateformes_sociales.remove(plateformes_sociales[2])
print(plateformes_sociales)
taille = 'Taille de la liste : ' + str(len(plateformes_sociales))
print(taille)


# Les dictionnaires
print('Ce qui fera suite est un traitement de dictionnaire : ')
taux_de_conversion ={}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
print(taux_de_conversion['facebook'])
print(taux_de_conversion)

del taux_de_conversion['instagram']
print('Après passage du del : ')
print(taux_de_conversion)

# Possibilité de tester occurence dans un dictionnaire :
print('poids' in taux_de_conversion)
print('facebook' in taux_de_conversion)
