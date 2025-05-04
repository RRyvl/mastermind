import tkinter as tk
from tkinter import Toplevel, Button, messagebox, Frame
import random as rd 
import json

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

# 1 joueur
COLORS = ["red", "blue", "yellow", "green", "orange", "purple"]
def gencode():
    return [rd.choice(COLORS) for i in range(4)]

code = gencode()

def open_page(title):
    """Ouvre une nouvelle fenêtre avec un titre et un bouton retour."""
    new_window = Toplevel(root)
    new_window.title(title)
    new_window.geometry("800x600")

        #Affichage des règles 
    if title == "Règles":
        regles_text = """ 
        LES REGLES DU JEU 
        L'objectif de ce jeu est de deviner la combinaison secrète composée de 4 couleurs. Chaque couleur est choisie parmi les 6 couleurs proposées 
            : red, blue, yellow, green, orange et purple. Les doublons sont autorisés. 
            A chaque tentative, vous obtenez un indice : 
            - rouge indique que une couleur est bien placée
            - blanc indique une couleur non existante
            - gris indique une bonne couleur mais mal placée 
            Vous avez 10 tentatives d'essais pour trouver la bonne combinaison. 

            Quel que ce soit le mode choisi, agrandissez la fenêtre pour voir la totalité du contenu de la fenêtre. 

            Pour le mode 2 joueurs, le joueur 1 doit entrer la combinaison secrète separees avec des espaces.  

            Bonne chance. 
        """
        label = tk.Label(new_window, text=regles_text, wraplength=700, justify = "left")
        label.pack(padx=20, pady=20)

    btn_return = Button(new_window, text="Retour Menu", command=new_window.destroy, height=2, width=10)
    btn_return.pack(side=tk.RIGHT, anchor="se", padx=20, pady=20)



def open_game(mode):
    """Ouvre la fenêtre de jeu avec grille et sélection de couleurs."""
    game_window = Toplevel(root)
    game_window.title(f"MasterMind - {mode}")
    game_window.geometry("800x600")
    code = [rd.choice(COLORS) for _ in range(4)]

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
        for j in range(4):
            cell = tk.Label(grid_frame, bg="white", width=8, height=4, borderwidth=2, relief="solid")
            cell.grid(row=i, column=j, padx=5, pady=5)
            row.append(cell)
        attempts.append(row)

     # Zone de feedback (affichage des indices)
    feedback_frame = tk.Frame(main_frame)
    feedback_frame.pack(side=tk.LEFT, padx=20)

    # Configuration de la grille de feedback pour que les cellules s'étendent
    for i in range(10):
        feedback_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):
        feedback_frame.grid_columnconfigure(j, weight=1)

    # Création d'une grille de feedback pour 10 lignes et 4 colonnes (indices)
    feedback_labels = []
    for i in range(10):
        row_feedback = []
        for j in range(4):
            cell = tk.Label(feedback_frame, bg="white", width=4, height=2, borderwidth=1, relief="solid")
            cell.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            row_feedback.append(cell)
        feedback_labels.append(row_feedback)

    # Zone d'entrée des couleurs
    entry_frame = tk.Frame(main_frame)
    entry_frame.pack(side=tk.RIGHT, padx=20)

    tk.Label(entry_frame, text="Choisissez 4 couleurs :").pack()

    selection_couleur = []
    ligne_actuelle = 0
    historique = []
    historique_guess = []
    save = []

        #Choix des deux modes
    if mode == "1 Joueur":
        code = [rd.choice(COLORS) for _ in range(4)]
    elif mode == "2 Joueurs":
        code = []
        def valider_code_joueur1():
            #Nonlocal signifie que nous voulons modifier la variable code de la fonction englobante open_game
            nonlocal code
            code_str = entry_code.get()
            code_temp = code_str.lower().split()
            if len(code_temp) != 4 or not all(c in COLORS for c in code_temp):
                messagebox.showerror("Erreur", "Entrez 4 couleurs valides séparées par un espace.")
                return
            code = code_temp
            top.destroy()
        
        top = Toplevel(root)
        top.title("Joueur 1 : Entrez un code")
        tk.Label(top, text="Entrez 4 couleurs parmi : " + ", ".join(COLORS)).pack(pady=10)
        entry_code = tk.Entry(top)
        entry_code.pack(pady=5)
        tk.Button(top, text="Valider", command=valider_code_joueur1).pack(pady=10)
        top.grab_set()
        top.wait_window()

    def sauvegarde():
        nonlocal code, save, historique_guess, ligne_actuelle, feedback_labels
        ligne_actuelle_copy = ligne_actuelle
        feedback_colors = [[cell.cget('bg') for cell in row] for row in feedback_labels]
        save = [historique_guess.copy(), ligne_actuelle_copy, feedback_colors, code.copy()]
        to_save = {
            "historique_guess": historique_guess,
            "ligne_actuelle": ligne_actuelle,
            "feedback_colors": feedback_colors,
            "code": code
        }

        with open("sauvegarde_mastermind.json", "w") as f:
            json.dump(to_save, f)

        messagebox.showinfo("Sauvegarde", "La partie a été sauvegardée avec succès.")

    def load():
        nonlocal code, ligne_actuelle, historique_guess, feedback_labels
        try:
            with open("sauvegarde_mastermind.json", "r") as f:
                to_save = json.load(f)
        except FileNotFoundError:
            messagebox.showwarning("Erreur", "Aucune sauvegarde trouvée.")
            return

        historique_guess = to_save["historique_guess"]
        ligne_actuelle = to_save["ligne_actuelle"]
        feedback_colors = to_save["feedback_colors"]
        code = to_save["code"]

        for cellule in range(len(historique_guess)):
            color = historique_guess[cellule]
            row = cellule // 4
            col = cellule % 4
            attempts[row][col].config(bg=color)
        for cellule in range(len(historique_guess), 40):
            row = cellule // 4
            col = cellule % 4
            attempts[row][col].config(bg='white')

        for i in range(10):
            for j in range(4):
                feedback_labels[i][j].config(bg=feedback_colors[i][j])

        messagebox.showinfo("La partie a été chargée ")

    def choisir_couleur(color):
        if len(selection_couleur) < 4:
            selection_couleur.append(color)
            update_color_display()

    def update_color_display():
        for i in range(4):
            color = selection_couleur[i] if i < len(selection_couleur) else "white"
            color_display[i].config(bg=color)

    def validate_combination():
        nonlocal code, ligne_actuelle, historique_guess
        if len(selection_couleur) != 4:
            messagebox.showerror("Erreur", "Veuillez sélectionner 4 couleurs")
            return

        # Affiche la combinaison dans la grille
        for i, color in enumerate(selection_couleur):
            attempts[ligne_actuelle][i].config(bg=color)
        historique_guess += selection_couleur.copy()
        feedback = matchcombi(selection_couleur, code)
        display_feedback(ligne_actuelle, feedback)
        historique.append((selection_couleur.copy(), feedback))
    

        if selection_couleur == code:
            messagebox.showinfo("Gagné", "Vous avez gagné")
            quitter()
        elif ligne_actuelle + 1 == 10:
            messagebox.showwarning("Perdu", "Vous avez perdu")
            quitter()
        else:
            # Passage à la prochaine tentative
            selection_couleur.clear()
            update_color_display()
            ligne_actuelle += 1

    def undo():
        nonlocal ligne_actuelle
        if ligne_actuelle > 0:
            ligne_actuelle -= 1
            for cellule in attempts[ligne_actuelle]:
                cellule.config(bg='white')
            for cellule in feedback_labels[ligne_actuelle]:
                cellule.config(bg='white')

    def help():
        nonlocal selection_couleur, code
        if ligne_actuelle == 0:
            messagebox.showinfo("Info", "Faites une première tentative avant d'utiliser l'aide.")
            return

        selection_couleur.clear()

        def est_valide(proposition):
            old_guess, old_feedback = historique[-1]
            return matchcombi(proposition, old_guess) == old_feedback


        essais = 0
        while True:
            color_pool_prio = []
            color_pool = COLORS[:]
            suggestion = []
            curseur = 0

            for case in feedback_labels[ligne_actuelle - 1]:
                prev_color = attempts[ligne_actuelle - 1][curseur].cget('bg')

                if case.cget("bg") == 'red':
                    suggestion.append(prev_color)
                elif case.cget("bg") == 'grey':
                    color_pool_prio.append(prev_color)
                    choix = rd.choice(color_pool_prio) if len(color_pool_prio) > 1 else rd.choice(color_pool)
                    while choix == prev_color and len(color_pool_prio) > 1:
                        choix = rd.choice(color_pool_prio)
                    suggestion.append(choix)
                else:
                    if prev_color in color_pool:
                        color_pool.remove(prev_color)
                    if color_pool_prio:
                        suggestion.append(rd.choice(color_pool_prio))
                    else:
                        suggestion.append(rd.choice(color_pool))
                curseur += 1

            essais += 1
            if est_valide(suggestion):
                break
            if essais > 1000:
                messagebox.showwarning("Impossible de générer une suggestion.")
                return

        selection_couleur.extend(suggestion)
        update_color_display()


    def matchcombi(guess, code_):
        feedback = ['white'] * 4
        code_copy = code_[:]
        guess_copy = guess[:]

    # Première passe : rouge (bien placé)
        for i in range(4):
            if guess[i] == code_[i]:
                feedback[i] = 'red'
                code_copy[i] = None
                guess_copy[i] = None

    # Deuxième passe : gris (mal placé)
        for i in range(4):
            if guess_copy[i] is not None and guess_copy[i] in code_copy:
                feedback[i] = 'grey'
                code_copy[code_copy.index(guess_copy[i])] = None
        return feedback




    def display_feedback(row, feedback):
        for i in range(4):
            feedback_labels[row][i].config(bg=feedback[i])

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
    btn_undo=tk.Button(entry_frame, text="Undo",command=undo)
    btn_undo.pack(pady=10)
    btn_help=tk.Button(entry_frame, text="Help",command=help)
    btn_help.pack(pady=10)
    btn_save=tk.Button(entry_frame, text="Save",command=sauvegarde)
    btn_save.pack(pady=10)
    btn_load=tk.Button(entry_frame, text="Load",command=load)
    btn_load.pack(pady=10)

# Lancement de l'application
root.mainloop()

