import timeit
import numpy as np
def rectangle_numpy(a,b,n,p1,p2,p3,p4,fonction): #rectangle avec numpy
    x = np.linspace(a,b,n+1)
    h = (b - a) / n
    Irect_numpy=0
    for j in range(0, len(x)):
        Irect_numpy += h * fonction(x[j]+ h/ 2,p1,p2,p3,p4)
    return Irect_numpy
def rectangle_math(a,b,n,p1,p2,p3,p4,fonction): #rectangle avec math
    h = (b-a)/n
    Irect_math = 0
    for i in range(1, n):
        Irect_math += h* fonction((a+(i*h))+h/2,p1,p2,p3,p4)
    return Irect_math
def mesurer_temps_rectangle(a,b,n,p1,p2,p3,p4,fonction): #calcul de temps d'excution
    temps_math_rect = timeit.timeit(lambda: rectangle_math(a,b,n,p1,p2,p3,p4,fonction), number=100000)
    resultat_math_rect = rectangle_math(a,b,n,p1,p2,p3,p4,fonction)
    temps_numpy_rect = timeit.timeit(lambda: rectangle_numpy(a,b,n,p1,p2,p3,p4,fonction), number=100000)
    resultat_numpy_rect = rectangle_numpy(a,b,n,p1,p2,p3,p4,fonction)
    return resultat_math_rect, temps_math_rect, resultat_numpy_rect, temps_numpy_rect