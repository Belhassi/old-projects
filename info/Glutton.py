##exo 3
def Allocation(Lc):
    Lc.sort()
    Ls = []

    for c in Lc:
        valider = False
        for s in Ls:
            if c[0] >= s[-1][1]:
                s.append(c)
                valider = True
                break
        if not valider:
            Ls.append([c])
    return Ls

Lc = [(1,2),(2,3),(2.5,4),(3,5),(4,6),(7,8)]
print(Allocation(Lc))


##exo 4
def Selection_activite(La):
    La.sort(key=lambda x: x[1])
    A = []
    hf = 0

    for a in La:
        if hf <= a[0]:
            A.append(a)
            hf = a[1]
    return A

print(Selection_activite(Lc))   
