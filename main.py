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


def code_aleatoire():
    code=[]
    couleurs=['red','blue','green','magenta','yellow','orange']
    for i in range(4):
        code+=[couleurs[rd.randint(0,5)]]
    return code
print(code_aleatoire())
        
root.mainloop()
