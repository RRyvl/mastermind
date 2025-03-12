import random as rd
import tkinter as tk
from tkinter import messagebox

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
        
root.mainloop()
