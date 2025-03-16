import tkinter as tk
import random
from tkinter import messagebox

# Liste des couleurs possibles
colors = ['red', 'blue', 'green', 'magenta', 'yellow', 'orange']

# Fonction pour générer une combinaison secrète
def generer_combinaison():
    return random.choices(colors, k=4)

# Fonction pour changer la couleur d'un bouton au clic
def changer_couleur(bouton):
    current_color = bouton.cget('bg')
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    bouton.config(bg=next_color)

# Fonction pour vérifier la combinaison entrée par le joueur
def verifier_combinaison():
    global ligne_actuelle

    # Récupérer la combinaison proposée par le joueur
    tentative = [bouton.cget('bg') for bouton in buttons[ligne_actuelle]]

    # Comparer avec la combinaison secrète
    rouges = sum([secret[i] == tentative[i] for i in range(4)])  # Bien placés
    blancs = sum(min(secret.count(c), tentative.count(c)) for c in set(secret)) - rouges  # Mal placés

    # Afficher le résultat dans l'historique
    liste_essais.insert(tk.END, f"Essai {ligne_actuelle+1}: {tentative} - {rouges} 🔴, {blancs} ⚪\n")

    # Désactiver la ligne actuelle
    for button in buttons[ligne_actuelle]:
        button.config(state=tk.DISABLED)

    # Vérifier si le joueur a gagné
    if rouges == 4:
        messagebox.showinfo("Gagné !", f"Bravo ! Vous avez trouvé la combinaison en {ligne_actuelle + 1} essais !")
        return

    # Passer à la ligne suivante si essais restants
    if ligne_actuelle < 9:
        ligne_actuelle += 1
        for button in buttons[ligne_actuelle]:
            button.config(state=tk.NORMAL)
    else:
        messagebox.showwarning("Perdu", f"Vous avez perdu ! La combinaison était {secret}")

# Fonction pour recommencer le jeu
def recommencer_jeu():
    global secret, ligne_actuelle

    # Générer une nouvelle combinaison secrète
    secret = generer_combinaison()
    ligne_actuelle = 0
    liste_essais.delete("1.0", tk.END)

    # Réinitialiser tous les boutons
    for i in range(10):
        for j in range(4):
            buttons[i][j].config(bg='red', state=tk.DISABLED)
    
    # Réactiver la première ligne
    for button in buttons[0]:
        button.config(state=tk.NORMAL)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Mastermind")

# Variables globales
secret = generer_combinaison()
ligne_actuelle = 0
buttons = []

# Interface de jeu
frame = tk.Frame(root)
frame.pack(pady=10)

# Création des boutons pour les essais
for i in range(10):
    row = []
    for j in range(4):
        bouton = tk.Button(frame, width=5, height=2, bg='red', state=tk.DISABLED)
        bouton.grid(row=i, column=j, padx=5, pady=5)
        bouton.config(command=lambda b=bouton: changer_couleur(b))  # Associer la fonction de changement de couleur
        row.append(bouton)
    buttons.append(row)

# Activer la première ligne
for bouton in buttons[0]:
    bouton.config(state=tk.NORMAL)

# Bouton de validation
valider_btn = tk.Button(root, text="Valider", command=verifier_combinaison)
valider_btn.pack(pady=10)

# Zone d'affichage des résultats
liste_essais = tk.Text(root, height=10, width=50)
liste_essais.pack()

# Bouton pour recommencer
btn_recommencer = tk.Button(root, text="Recommencer", command=recommencer_jeu)
btn_recommencer.pack(pady=5)

import tkinter as tk
import random

def open_game(mode):
    """Ouvre la fenêtre correspondante en fonction du mode de jeu choisi."""
    if mode == "1 Joueur":
        ouvrir_mode_1joueur()
    elif mode == "2 Joueurs":
        ouvrir_mode_2joueurs()

def ouvrir_mode_1joueur():
    """Crée une fenêtre pour le mode 1 joueur."""
    nouvelle_fenetre = tk.Toplevel(root)
    nouvelle_fenetre.title("Mode 1 Joueur")
    nouvelle_fenetre.geometry("800x800")
    
    #Titre et description du mode
    label = tk.Label(nouvelle_fenetre, text="Mode 1 Joueur", font=("Arial", 16))
    label.pack(pady=50)

    #Créer une liste de variables pour stocker la couleur de chaque carré
    couleur_choisie = [tk.StringVar(value="red") for _ in range(4)]
    
    #Liste de couleurs disponibles
    couleurs = ["red", "blue", "green", "magenta", "yellow", "orange"]
    
    # Fonction pour changer la couleur d'un carré
    def changer_couleur(i):
        """Change la couleur du carré i lorsque l'utilisateur clique sur le bouton couleur."""
        current_color = couleur_choisie[i].get()
        next_color = couleurs[(couleurs.index(current_color) + 1) % len(couleurs)]
        couleur_choisie[i].set(next_color)
        color_buttons[i].config(bg=next_color)

    # Créer les carrés pour sélectionner les couleurs (dans une grille)
    color_buttons = []
    for i in range(10):
        row=[]
        for j in range(4):
            button = tk.Button(nouvelle_fenetre, width=3, height=1, bg="red", command=lambda i=i,j=j: changer_couleur(i,j))
            button.pack(row=i, column=j, padx=5, pady=5)
            row.append(button)
        color_buttons.append(button)

    #Bouton pour valider la combinaison choisie
    def valider_combinaison():
        combinaison = [couleur_choisie[i].get() for i in range(4)]
        print(f"Combinaison choisie : {combinaison}")
        # Vous pouvez ajouter la logique ici pour vérifier la combinaison ou commencer le jeu
        nouvelle_fenetre.quit()  # Ferme la fenêtre après validation

    valider_btn = tk.Button(nouvelle_fenetre, text="Valider", command=valider_combinaison, font=("Arial", 12))
    valider_btn.pack(pady=20)

def ouvrir_mode_2joueurs():
    """Crée une fenêtre pour le mode 2 joueurs."""
    nouvelle_fenetre = tk.Toplevel(root)
    nouvelle_fenetre.title("Mode 2 Joueurs")
    nouvelle_fenetre.geometry("800x600")
    
    #Titre et description du mode
    label = tk.Label(nouvelle_fenetre, text="Mode 2 Joueurs", font=("Arial", 16))
    label.pack(pady=50)
    
    #Exemple d'éléments interactifs pour 2 joueurs
    instruction_label = tk.Label(nouvelle_fenetre, text="Joueur 1, entrez votre combinaison :", font=("Arial", 12))
    instruction_label.pack(pady=10)

    #Champ de saisie pour le joueur 1
    combinaison_entry1 = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
    combinaison_entry1.pack(pady=10)

    #Bouton pour le joueur 1 pour valider la combinaison
    def valider_combinaison1():
        combinaison1 = combinaison_entry1.get()
        print(f"Joueur 1, combinaison entrée : {combinaison1}")
        instruction_label.config(text="Joueur 2, entrez votre combinaison :")  # Change le texte pour Joueur 2
        combinaison_entry1.delete(0, tk.END)  # Réinitialiser le champ de saisie pour Joueur 1

    valider_btn1 = tk.Button(nouvelle_fenetre, text="Valider Joueur 1", command=valider_combinaison1, font=("Arial", 12))
    valider_btn1.pack(pady=20)

    #Champ de saisie pour le joueur 2
    combinaison_entry2 = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
    combinaison_entry2.pack(pady=10)

    #Bouton pour le joueur 2 pour valider la combinaison
    def valider_combinaison2():
        combinaison2 = combinaison_entry2.get()
        print(f"Joueur 2, combinaison entrée : {combinaison2}")
        nouvelle_fenetre.quit()  # Fermer la fenêtre après que les deux joueurs ont entré leur combinaison

    valider_btn2 = tk.Button(nouvelle_fenetre, text="Valider Joueur 2", command=valider_combinaison2, font=("Arial", 12))
    valider_btn2.pack(pady=20)

#Fenêtre principale
root = tk.Tk()
root.title("Menu Principal")
root.geometry("300x200")

#boutons pour choisir le mode de jeu
btn_1_joueur = tk.Button(root, text="1 Joueur", command=lambda: open_game("1 Joueur"), height=2, width=15)
btn_1_joueur.pack(pady=10)

btn_2_joueur = tk.Button(root, text="2 Joueurs", command=lambda: open_game("2 Joueurs"), height=2, width=15)
btn_2_joueur.pack(pady=10) 

def generer_combinaison():
    # Génère une combinaison secrète avec des couleurs parmi une liste. 
    couleurs = ["red" ,"blue" ,"green" ,"magenta" ,"yellow" ,"orange"]
    return random.choices(couleurs, k=4)  # cela permet les repetitions et genere automatiquement une combinaison de 4 couleurs

def verifier_combinaison(secret, tentative):
    # Compare la tentative du joueur avec la combinaison secrète. 
    rouges = sum([s == t for s, t in zip(secret, tentative)])  # Bien placés
    blancs = sum([min(secret.count(c), tentative.count(c)) for c in set(tentative)]) - rouges  # Mal placés
    return rouges, blancs

# Initialisation
secret = generer_combinaison()
essais_max = 10
gagne = False

print("Trouvez la combinaison de 4 couleurs.")

for essai in range(1, essais_max + 1):
    # Demande à l'utilisateur une proposition
    tentative = input(f"Essai {essai}/{essais_max} - Entrez 4 couleurs : ").split()

    if len(tentative) != 4:
        print("Veuillez entrer exactement 4 couleurs.")
        continue

    rouges, blancs = verifier_combinaison(secret, tentative)
    print(f"Résultat : {rouges} 🔴 (bien placés), {blancs} ⚪  (mal placés)")

    if rouges == 4:
        print(f"Bien joué ! Vous avez trouvé la combinaison {secret} en {essai} essais.")
        gagne = True
        break
print(secret)

# MODE 2 JOUEURS
def deux_joueurs(colors):#la fonction permet au premier joueur de créer un code
    while True:
        code = input('Choisissez 4 couleur parmis : red ,blue ,green ,magenta ,yellow ,orange: ').split()
        if len(code) != 4:
            print("Choisissez 4 couleur !")
        elif any(color not in colors for color in code):
            print("couleur invalid")
        else:
            return  code

# MODE 2 JOUEURS
def deux_joueurs(colors):#la fonction permet au premier joueur de créer un code
    while True:
        code = input('Choisissez 4 couleur parmis : red ,blue ,green ,magenta ,yellow ,orange: ').split()
        if len(code) != 4:
            print("Choisissez 4 couleur !")
        elif any(color not in colors for color in code):
            print("couleur invalid")
        else:
            return  code

root.mainloop()

