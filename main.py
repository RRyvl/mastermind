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

# Lancer l'interface
root.mainloop()
