import random as rd
import tkinter as tk

def ouvrir_page_vide1():
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title("1 joueur")
def ouvrir_page_vide2():
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title("2 joueur")
def ouvrir_page_regle():
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title("Règles")
def quitter():
    root.quit()

root = tk.Tk()
root.title("Mastermind")
root.geometry("300x200")

titre = tk.Label(root, text="Mastermind", font=("Arial", 20))
titre.pack(pady=20)

sous_titre = tk.Label(root, text="Menu", font=("Arial", 14))
sous_titre.pack(pady=10)

btn_1joueur = tk.Button(root, text="1 Joueur", command=ouvrir_page_vide1)
btn_1joueur.pack(pady=5)

btn_2joueurs = tk.Button(root, text="2 Joueurs", command=ouvrir_page_vide2)
btn_2joueurs.pack(pady=5)

btn_quitter = tk.Button(root, text="Quitter", command=quitter)
btn_quitter.place(x=10, y=170)

btn_regle = tk.Button(root, text="Règles", command=ouvrir_page_regle)
btn_regle.place(x=250, y=170)


import random as rd
def code_aleatoire():
    code=[]
    couleurs=['red','blue','green','magenta','yellow','orange']
    for i in range(4):
        code+=[couleurs[rd.randint(0,5)]]
    return code

def jeu_solo(tour): #on initialise la fonction qui permet au joueur de deviner un code
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
        
jeu_solo(10)
        
root.mainloop()
