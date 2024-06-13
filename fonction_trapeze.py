import numpy as np
import timeit
def trapeze_numpy(a,b,n,p1,p2,p3,p4,fonction): #trapeze avec numpy
    x = np.linspace(a,b,n+1)
    y = fonction(x,p1,p2,p3,p4)
    Itrap_numpy = np.trapz(y,x)
    return Itrap_numpy
def trapeze_math(a,b,n,p1,p2,p3,p4,fonction): #trapeze avec math
    h = (b-a)/n
    Itrap_math = (fonction(a,p1,p2,p3,p4)+fonction(b,p1,p2,p3,p4)) / 2
    for i in range(1, n):
        Itrap_math += fonction(a+i*h,p1,p2,p3,p4)
    Itrap_math *= h
    return Itrap_math
def mesurer_temps_integral(a,b,n,p1,p2,p3,p4,fonction): #calcul de temps d'excution
    temps_math = timeit.timeit(lambda: trapeze_math(a,b,n,p1,p2,p3,p4,fonction), number=100000)
    resultat_math = trapeze_math(a,b,n,p1,p2,p3,p4,fonction)
    temps_numpy = timeit.timeit(lambda: trapeze_numpy(a,b,n,p1,p2,p3,p4,fonction), number=100000)
    resultat_numpy = trapeze_numpy(a,b,n,p1,p2,p3,p4,fonction)
    return resultat_math, temps_math, resultat_numpy, temps_numpy