import tkinter as tk
from tkinter import Toplevel, Button, messagebox, Frame

# Création de la fenêtre principale
root = tk.Tk()
root.title("MasterMind")
root.geometry("800x600")
root.minsize(800, 600)

# Activation du redimensionnement
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Titre
title_label = tk.Label(root, text="MasterMind", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

# Boutons pour choisir le mode de jeu
btn_1_joueur = tk.Button(root, text="1 Joueur", command=lambda: open_game("1 Joueur"), height=2, width=15)
btn_1_joueur.pack(pady=10)

btn_2_joueur = tk.Button(root, text="2 Joueurs", command=lambda: open_game("2 Joueurs"), height=2, width=15)
btn_2_joueur.pack(pady=10)

# Bas de page (quitter et règles)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

def quitter():
    """Ferme l'application."""
    root.destroy()

btn_quitter = tk.Button(bottom_frame, text="Quitter", command=quitter, height=2, width=10)
btn_quitter.pack(side=tk.LEFT, anchor="sw")

btn_regles = tk.Button(bottom_frame, text="Règles", command=lambda: open_page("Règles"), height=2, width=10)
btn_regles.pack(side=tk.RIGHT, anchor="se")


#1 joueur

COLORS = ["red", "blue", "yellow", "green", "orange", "purple"]


def open_game(mode):
    """Ouvre la fenêtre de jeu avec grille et sélection de couleurs."""
    game_window = Toplevel(root)
    game_window.title(f"MasterMind - {mode}")
    game_window.geometry("800x600")

    btn_return = Button(game_window, text="Retour Menu", command=game_window.destroy, height=2, width=10)
    btn_return.pack(side=tk.RIGHT, anchor="se", padx=20, pady=20)

    # Cadre principal
    main_frame = tk.Frame(game_window)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Grille des tentatives
    grid_frame = tk.Frame(main_frame)
    grid_frame.pack(side=tk.LEFT, padx=20)

    attempts = []
    for i in range(10):
        row = []
        for j in range(5):
            cell = tk.Label(grid_frame, bg="white", width=8, height=4, borderwidth=2, relief="solid")
            cell.grid(row=i, column=j, padx=5, pady=5)
            row.append(cell)
        attempts.append(row)
    for i in range(10):
        row = []
        cell = tk.Label(grid_frame, bg="gray", width=8, height=4, borderwidth=2, relief="solid")
        cell.grid(row=i, column=j, padx=5, pady=5)
        row.append(cell)
    attempts.append(row)

    # Zone d'entrée des couleurs
    entry_frame = tk.Frame(main_frame)
    entry_frame.pack(side=tk.RIGHT, padx=20)

    tk.Label(entry_frame, text="Choisissez 4 couleurs :").pack()

    selection_couleur = []
    ligne_actuelle = 0

    def choisir_couleur(color):
        if len(selection_couleur) < 4:
            selection_couleur.append(color)
            update_color_display()

    def update_color_display():
        for i in range(4):
            color = selection_couleur[i] if i < len(selection_couleur) else "white"
            color_display[i].config(bg=color)

    def validate_combination():
        nonlocal ligne_actuelle 
        if len(selection_couleur) == 4:
            for i, color in enumerate(selection_couleur):
                attempts[ligne_actuelle ][i].config(bg=color)
            selection_couleur.clear()
            update_color_display()
            ligne_actuelle  += 1
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner 4 couleurs")


    # Affichage des 4 couleurs sélectionnées
    color_display = [tk.Label(entry_frame, bg="white", width=8, height=4, borderwidth=2, relief="solid") for _ in range(4)]
    for lbl in color_display:
        lbl.pack(side=tk.LEFT, padx=5)

    # Boutons de sélection des couleurs
    color_frame = tk.Frame(entry_frame)
    color_frame.pack(pady=10)

    for i, color in enumerate(COLORS):
        btn = tk.Button(color_frame, text=color, bg=color, width=10, height=2, command=lambda c=color: choisir_couleur(c))
        btn.grid(row=i, column=0, padx=5, pady=5)

    # Bouton de validation
    btn_valider = tk.Button(entry_frame, text="Valider", command=validate_combination)
    btn_valider.pack(pady=10)

    # Bouton Retour Menu
    Button(game_window, text="Retour Menu", command=game_window.destroy).pack(side=tk.RIGHT, anchor="se", padx=20, pady=20)

def quitter():
    """Ferme l'application."""
    root.destroy()

# Lancement de l'application
root.mainloop()



        

