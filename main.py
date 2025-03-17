import random as rd
import tkinter as tk
from tkinter import messagebox
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

btn_quitter = tk.Button(bottom_frame, text="Quitter", command=quitter, height=2, width=10)
btn_quitter.pack(side=tk.LEFT, anchor="sw")

btn_regles = tk.Button(bottom_frame, text="Règles", command=lambda: open_page("Règles"), height=2, width=10)
btn_regles.pack(side=tk.RIGHT, anchor="se")

def quitter():
    """Ferme l'application."""
    root.destroy()


COLORS = ["red", "blue", "yellow", "green", "orange", "purple"]

def open_game(mode):
    """Ouvre la fenêtre de jeu avec grille et sélection de couleurs."""
    game_window = Toplevel(root)
    game_window.title(f"MasterMind - {mode}")
    game_window.geometry("800x600")

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

    def select_color(color):
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
        btn = tk.Button(color_frame, text=color, bg=color, width=10, height=2, command=lambda c=color: select_color(c))
        btn.grid(row=i, column=0, padx=5, pady=5)

    # Bouton de validation
    btn_valider = tk.Button(entry_frame, text="Valider", command=validate_combination)
    btn_valider.pack(pady=10)

    # Bouton Retour Menu
    Button(game_window, text="Retour Menu", command=game_window.destroy).pack(side=tk.RIGHT, anchor="se", padx=20, pady=20)




ligne_actuelle=0
colors=['red','blue','green','magenta','yellow','orange']
def changer_couleur(bouton,i,j):
    global colors
    current_color = bouton.cget('bg')
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    bouton.config(bg=next_color)
    
def valider_ligne(i,buttons,fenetre,code): 
    for button in buttons[i]:
        button.config(state=tk.DISABLED)
    guess=[bouton.cget('bg') for bouton in buttons[i]]
    if i+1<10 and guess!=code:
        for button in buttons[i+1]:
            button.config(state=tk.NORMAL)
    elif guess!=code and i+1>=10:
        messagebox.showwarning("Perdu","Vous avez perdu")
        fenetre.destroy()
    else :
        messagebox.showwarning("Gagné!",'Vous avez gagné')
        
        
    global ligne_actuelle
    ligne_actuelle+=1

            

def ouvrir_page_vide1():
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title("1 joueur")
    code_partie=gencode()
    buttons = []
    resultat = []
    for i in range(10):
        row = []
        for j in range(4):
            bouton = tk.Button(nouvelle_fenetre, width=5, height=2, bg='red', state=tk.DISABLED)
            bouton.grid(row=i, column=j, padx=5, pady=5)
            bouton.config(command=lambda bouton=bouton, i=i, j=j: changer_couleur(bouton, i, j))
            row.append(bouton)
        buttons.append(row)    
    for bouton in buttons[0]:
        bouton.config(state=tk.NORMAL)
    global ligne_actuelle   
    valider_btn = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: valider_ligne(ligne_actuelle,buttons,nouvelle_fenetre,code_partie))
    valider_btn.grid(row=10, column=0, columnspan=4, pady=20)
    
    

def gencode():
    return [rd.choice(colors) for i in range(4)]


'''def jeu_solo(tour): #on initialise la fonction qui permet au joueur de deviner un code
    reponse=code_aleatoire()
    print(reponse)
    historique_guess=[]
    historique_match=[]
    for i in range(tour): #le joueur a "10 vies"
        guess=[]
        for i in range(4): 
            guess+=[input('Choisissez une couleur parmis : red ,blue ,green ,magenta ,yellow ,orange: ')]
        historique_guess+=[guess]
        match=[] #liste correspondant au test de chacune des couleurs
        for indice in range(len(guess)):
            if guess[indice]==reponse[indice]:
                match+=["green"]
            elif guess[indice] in reponse:
                match+=["yellow"]
            else:
                match+=["red"]
        historique_match+=[match]
        if match==["green","green","green","green"]:
            print('Gagné')
            return('Gagné')
        print(match)
    print('Perdu')
    return('Perdu')
        
jeu_solo(10)'''



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
