
## exemple top down
def Fib(n, d={}): 
    if n < 2 :
        return n
    if n in d:
        return d[n]
    else:
        d[n] = Fib(n-1, d) + Fib(n-2, d)
        return d[n]

def fact(n, d={}):
    if n == 0 or n == 1:
        return 1
    elif n in d:
        return d[n]
    else:
        d[n] = n*fact(n-1)
        return d[n]
    
def minimaliste(L):
    if len(L) != 1:
        return L[0]
    else:
        x = L.pop(0)
        return min(x, minimalist(L))
        
def minimalisteTD(L):
    n = len(L)
    if n == 1:
        return L[0]
    elif n in D:
        return D[n]
    else:
        n = L.pop(0)
        D[n] = min(x, minimalist(L))
        return D[n]

        
##Bottom down
def Fib_down(n):
    L = []
    for i in range(2, n+1, 1):
        L.append(L[-1] + L[-2])
    return L[n]

def minimaliste(L):
    R = [L[0]]
    n = len(L)
    for i in range(1, n, 1):
        R.append(min(R[-1], L[i]))

    return R[n-1]



##exo 6
def rendre_monnies(P, s):
    L = ['inf']*(s+1)
    L[0] = 0
    for i in range(1, s+1, 1):
        for x in P:
            if x <= i:
                L[i] = min(L[i], L[i-n]+1)

### distance de livenshtein
def d_liv_BUP(s1, s2):
    m = len(s1)
    n = len(s2)
    
    M = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        M[i][0] = i 
    for j in range(n+1):
        M[i][0] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:  cout = 0
            else:   cout = 1

            M[i][j] = min(M[i-1][j] +1, M[i][j-1] +1, M[i-1][j-1]+cout)
    return M[m][n]

s1 = 'imad'
s2 = 'othmane'

print(d_liv_BUP(s1, s2))