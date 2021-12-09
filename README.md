# Python
Visualisation des branches git branch

On choisit la branche sur laquelle on veut se placer git checkout test

On regarde si on a du dev en cours git status

On se met à jour depuis le serveur git pour éviter d’écraser le dev de tout le monde -> c’est pas gentil et ça fait des conflits git pull origin test

Dans le cas où on a créé un fichier / dossier git add nom_du_fichier

On valide sa branche locale git commit -am "livraison test claire et précis"

On récupère notre joli dev bien commenté depuis notre branche de dev git merge dev

On envoi vers le serveur git git push origin test

Penser à bien installer git avant d'ouvrir Pycharm :D  