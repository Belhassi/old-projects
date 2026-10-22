from graphes import *

def insertion(A, pos, x):
    if pos == 'g':
        A[1] = [x, None, None]
    elif pos == 'd':
        A[2] = [x, None, None]

def Inordre(A):
    if A == None:
        return []
    
    return Inordre(A[1]) + [A[0]] + Inordre(A[2])

def preordre(A):
    if A == None:
        return []
    
    return [A[0]] + preordre(A[1]) + preordre(A[2])

def postordre(A):
    if A == None:
        return []
    
    return postordre(A[1]) + postordre(A[2]) + [A[0]]

def niveau(A, N):
    if N == 0:
        print(A[0], end=' ')
    else:
        niveau(A[1], N-1)
        niveau(A[2], N-1)    

def nbrNoeudniveau(A, N):
    if A != None:
        if N == 0:
            return 1
        else:
            n1 = nbrNoeudniveau(A[1], N-1)
            n2 = nbrNoeudniveau(A[2], N-1)
            
            return n1+n2
    return 0

def nbrNiveau(A):
    compteur = 0
    while nbrNoeudniveau(A, compteur) != 0:
        compteur += 1
    return compteur

def nbrNoeud(A):
    compteur = 0
    i = nbrNiveau(A)
    while i >= 0 :
        compteur += nbrNoeudniveau(A, i)
        i = i-1
    return compteur

def affichage(A):
    for i in range(nbrNiveau(A)):
        niveau(A, i)

def chercher(A, x):
    if A != None:
        if A[0] == x:
            return True
        else:
            return chercher(A[1], x) or chercher(A[2], x)
    else:
        return False

def listeDeNoeudsParNiveau(A, N):
    if A != None:
        if N == 0:
            return [A[0]]
        else:
            return listeDeNoeudsParNiveau(A[1], N-1) + listeDeNoeudsParNiveau(A[2], N-1)
            
    else:
        return []

def ParfaitComplet(A): # A est dit parfait complet si tous les niveau sont totalement remplis
    n = nbrNiveau(A)
    for i in range(n):
        if nbrNoeudniveau(A, i) != 2**i:
                return False
    return True

def parfait(A):# A est dit parfait complet si tous les niveau sont totalement remplis sauf le dernier dont les element sont groupe a gauche
    pass


###########
def gauche(i):
    return 2*i +1

def droite(i):
    return 2*i +2

def pere(i):
    return (i-1)//2

def maximum(T,i,limite):
    imax = i
    if gauche(i) < limite and T[gauche(i)] > T[imax]:
        imax = gauche(i)
    if droite(i) < limite and T[droite(i)] > T[imax]:
        imax = droite(i)

    return imax

def entasser(T, i, limite):
    imax = maximum(T,i,limite)
    if imax != i:
        T[i], T[imax] = T[imax], T[i]
        entasser(T, imax, limite)

def construireTas(T):
    n = len(T)
    for i in range(n-1,-1,-1):
        entasser(T, i, n)

def estunTas(T):
    for i in range(1, len(T)):
        if T[i] > T[pere(i)]:
            return False
    return True

def TrierTas(T):
    n = len(T)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        entasser(T,0,n)

def TrierParTas(T):
    if not estunTas(T):
        construireTas(T)
    TrierTas(T)
        



###########
A = [5 ,None, None]
insertion(A, 'g', 2)
insertion(A, 'd', 6)
insertion(A[1], 'd', 1)
insertion(A[1], 'g', 0)
insertion(A[2], 'd', 1)
insertion(A[2], 'g', 9)
insertion(A[1][1], 'g', 5)

T = [1,2,5,6,3,1,0,8]
TrierParTas(T)
print(T)
