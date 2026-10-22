## parcours d'un graphe
from random import *

def BFS(G, s):
    L = [s]
    d = {s:None}

    while L != []:
        u = L.pop(0)
        for v in G[u]:
           if v not in d:
               L.append(v)
               d[v] = u
    return d

def DFS(G, s):
    L = [s]
    d = {s:None}
    
    while L != []:
        u = L[-1]
        Lv = []
        for v in G[u]:
            if v not in d:
                Lv.append(v)
        if Lv != []:
            v = choice(Lv)
            L.append(v)
            d[v] = u
        else:
            L.pop(-1)
    return d

## Q3
def chercher(G, x):
    return x in G

## Q4
def OrdreSommet(G):
    return len(G)

## Q5
def DegreSommet(G,s):
    return len(G[s])

## Q6
def Adjacences(G, s1, s2):
    return s1 in G[s2] or s2 in G[s1]

## Q7
def comporteBoucle(G):
    for u in G:
        if u in G[u]:
            return True
    return False

## Q8
def grapheSimple(M):
    m = len(M)
    for i in range(n):
        if M[i][i] != 0:
            return False
        for j in range(n):
            if M[i][j] > 1:
                return False
    return True

## Q9
def admetChaineEulerienne(G):
    pass


if __name__ == "__main__":
    G = {'a':['b','d', 'e'],'b':['a', 'c'],'c':['b','d'],'e':['d', 'g', 'f'], 'h':['g'], 'd':['c','a', 'e'], 'g':['e','f','h'], 'f':['e', 'h']}
    print(BFS(G, 'a'))
    print(DFS(G, 'a'))


