import random as rd
def code_aleatoire():
    code=[]
    couleurs=['red','blue','green','magenta','yellow','orange']
    for i in range(4):
        code+=[couleurs[rd.randint(0,5)]]
    return code
print(code_aleatoire())
        
