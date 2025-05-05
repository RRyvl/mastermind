MI TD-01
Ela 
Romain 
Aiswarya Collaty
                                        MASTERMIND 
L’url : https://github.com/RRyvl/mastermind/blob/main/main.py
                 
L’objectif principal est de deviner une combinaison secrète de 4 couleurs en un maximum de 10 tentatives. 
LANCEMENT DU PROGRAMME
Une fenêtre principale s’ouvre avec le menu du jeu après avoir exécuté le fichier python contenant le code. 
INTERFACE PRINCIPALE 
Titre : Mastermind 
Boutons de sélection : 
-	1 joueur : l’ordinateur génère la combinaison secrète. 
-	2 joueurs : un joueur essaye de deviner la combinaison secrète. 
-	Règles : affiche les règles du jeu
-	Quitter : ferme la fenêtre du jeu
MODE DE JEU 
Mode 1 joueur : Une combinaison de 4 couleurs est générée aléatoirement. Il faut deviner cette combinaison en cliquant sur des couleurs qui sont proposées, puis sur valider. 
Mode 2 joueurs : le joueur 1 entre manuellement une combinaison (via une autre fenêtre qui va s’ouvrir automatiquement). Le joueur 2 doit essayer de retrouver cette combinaison comme dans le mode 1 joueur. 
REGLES DU JEU 
En cliquant sur règles, une nouvelle fenêtre s’ouvre : 
-	6 couleurs disponible: red, blue, yellow, green, orange, purple. 
-	Il faut créer une combinaison de 4 couleurs. 
-	Les doublons sont autorisés. 
-	Chaque tentative donne un feedback de couleurs : 
-rouge : couleur bien placée 
-blanc : couleur non existante
-gris : bonne couleur mais mal placée 
- Le joueur a un maximum de 10 essais pour trouver la bonne combinaison. 

INTERFACE DE JEU
-	Sélection des couleurs : clique sur les boutons colores
-	Valider : envoie la tentative faite par le joueur
-	Undo : efface la dernière ligne entrée 
-	Help : donne une aide de combinaison en fonction des essais précédents. 
-	Save : sauvegarde la partie dans un fichier appelé : « sauvegarde_mastermind.json 
-	Load : recharge la partie sauvegardée. 

SAUVEGARDE ET CHARGEMENT 
-	Le fichier sauvegarde_mastermind.json contient : 
-les combinaisons précédentes
-les feedbacks
-le code secret
-le numéro de la tentative en cours 


FIN DE PARTIE 
-	Victoire si le joueur trouve la bonne combinaison. 
-	Apres 10 essais le joueur perd. 

Bibliothèques : tkinter, random, json
