import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import fonction_trapeze as tr
import fonction_rectangle as rec
import fonction_simpson as simp
def fonction(x,p1,p2,p3, p4): #definir le polynome
    return p1+ p2*x + p3* x**2 + p4 * x**3
def integrale_exacte(a,b,p1,p2,p3,p4): #calcul d'integral analytique
    integral_analytique = (p1*(b-a) + (p2/2) * (b**2 - a**2) + (p3/3) * (b**3-a**3) + (p4/4) * (b**4 - a**4))
    return integral_analytique


def main():
    #entrer les bornes et les coefficients :
    while True:
        try:
            a = float(input("entrez la borne inférieure de l'intégrale:"))
            b = float(input("entrez la borne supérieure de l'intégrale:"))
            p1 = float(input("entrez le coefficient P1:"))
            p2 = float(input("entrez le coefficient P2:"))
            p3 = float(input("entrez le coefficient P3:"))
            p4 = float(input("entrez le coefficient P4:"))
            break
        except ValueError:
            print("entrez des valeurs numériques :")
    while True:
        try:
            n = int(input("entrez le nombre de segments :"))
            break
        except ValueError:
            print("entrez un entier")

    #calcul des intégrales et temps:
    #méthode trapèzes
    resultat_math, temps_math, resultat_numpy, temps_numpy = tr.mesurer_temps_integral(a,b,n,p1,p2,p3,p4,fonction)
    print(f'Résultats avec la méthode des trapèzes')
    print(f"résultat avec numpy : {resultat_numpy}, temps d'exécution : {temps_numpy:.6f} secondes") #temps en sec avec 6 chiffres apres virgule
    print(f"résultat avec math : {resultat_math}, temps d'exécution : {temps_math:.6f} secondes")

    #méthode rectangles
    resultat_math_rect, temps_math_rect, resultat_numpy_rect, temps_numpy_rect = rec.mesurer_temps_rectangle(a, b, n, p1, p2, p3, p4,fonction)
    print(f'Résultats avec la méthode des rectangles')
    print(f"résultat avec numpy : {resultat_numpy_rect}, temps d'exécution : {temps_numpy_rect:.6f} secondes")  # temps en sec avec 6 chiffres apres virgule
    print(f"résultat avec math : {resultat_math_rect}, temps d'exécution : {temps_math_rect:.6f} secondes")

    #méthode simpson
    resultat_math_simpson, temps_math_simpson, resultat_numpy_simpson, temps_numpy_simpson, temps_scipy_simpson, resultat_scipy_simpson = simp.mesurer_temps_simpson(a, b, n, p1, p2, p3 ,p4, fonction)
    print(f'Résultats avec la méthode Simpson')
    print(f"résultat avec numpy : {resultat_numpy_simpson}, temps d'exécution : {temps_numpy_simpson:.6f} secondes")  # temps en sec avec 6 chiffres apres virgule
    print(f"résultat avec math : {resultat_math_simpson}, temps d'exécution : {temps_math_simpson:.6f} secondes")
    print(f'résultat avec scipy : {resultat_scipy_simpson}, temps d\'exécution : {temps_scipy_simpson:.6f} secondes')
    #intégrale exacte
    Iexact = integrale_exacte(a,b,p1,p2,p3,p4)
    print(f"Solution exacte : {Iexact}")

    #donnée pour les graphes :
    segments = np.arange(10, 1000, 10)
    erreur_trapeze_math = []
    erreur_trapeze_numpy = []
    erreur_rectangle_math = []
    erreur_rectangle_numpy = []
    erreur_simpson_math = []
    erreur_simpson_numpy = []
    erreur_simpson_scipy = []
    temps_trapeze_math = []
    temps_trapeze_numpy = []
    temps_rectangle_math = []
    temps_rectangle_numpy = []
    temps_simpson_math = []
    temps_simpson_numpy = []
    temps_simpson_scipy = []
    res_trapeze_math = []
    res_trapeze_numpy = []
    res_rectangle_math = []
    res_rectangle_numpy = []
    res_simpson_math = []
    res_simpson_numpy = []
    res_simpson_scipy = []

    for n in segments:
        resultat_math, temps_math, resultat_numpy, temps_numpy = tr.mesurer_temps_integral(a,b,n,p1,p2,p3,p4,fonction)
        resultat_math_rect, temps_math_rect, resultat_numpy_rect, temps_numpy_rect = rec.mesurer_temps_rectangle(a, b,n, p1,p2, p3,p4,fonction)
        resultat_math_simpson, temps_math_simpson, resultat_numpy_simpson, temps_numpy_simpson, temps_scipy_simpson, resultat_scipy_simpson = simp.mesurer_temps_simpson(a, b, n, p1, p2, p3, p4, fonction)
        temps_trapeze_math.append(temps_math)
        erreur_trapeze_math.append(abs(resultat_math - Iexact))
        res_trapeze_math.append(resultat_math)
        temps_trapeze_numpy.append(temps_numpy)
        erreur_trapeze_numpy.append(abs(resultat_numpy - Iexact))
        res_trapeze_numpy.append(resultat_numpy)
        temps_rectangle_math.append(temps_math_rect)
        erreur_rectangle_math.append(abs(resultat_math_rect - Iexact))
        res_rectangle_math.append(resultat_math_rect)
        temps_rectangle_numpy.append(temps_numpy_rect)
        erreur_rectangle_numpy.append(abs(resultat_numpy_rect - Iexact))
        res_rectangle_numpy.append(resultat_numpy_rect)
        temps_simpson_math.append(temps_math_simpson)
        erreur_simpson_math.append(abs(resultat_math_simpson - Iexact))
        res_simpson_math.append(resultat_math_simpson)
        temps_simpson_numpy.append(temps_numpy_simpson)
        erreur_simpson_numpy.append(abs(resultat_numpy_simpson - Iexact))
        res_simpson_numpy.append(resultat_numpy_simpson)
        temps_simpson_scipy.append(temps_scipy_simpson)
        erreur_simpson_scipy.append(abs(resultat_scipy_simpson -Iexact))
        res_simpson_scipy.append(resultat_scipy_simpson)

    # ggraph de convergence
    plt.figure(figsize=(10, 6))
    plt.plot(segments, erreur_trapeze_math, color='c', label='trapèze math')
    plt.plot(segments, erreur_trapeze_numpy, color='blue',label='trapèze numpy')
    plt.plot(segments, erreur_rectangle_math, color='yellow', label='rectangle math')
    plt.plot(segments, erreur_rectangle_numpy, color='green', label='rectangle numpy')
    #plt.plot(segments, erreur_simpson_math, color='orange', label='simpson math')
    plt.plot(segments, erreur_simpson_numpy, color='red', label='simpson numpy')
    #plt.plot(segments, erreur_simpson_scipy, color='pink', label='simpson scipy')
    plt.xlabel('nombre des segments')
    plt.ylabel("l'erreur")
    plt.yscale('log')
    plt.title('convergence')
    plt.legend()
    plt.grid(True)

    #graph du temps d'excution
    plt.figure(figsize=(10, 6))
    plt.plot(segments, temps_trapeze_math, color='c', label='trapèze math')
    plt.plot(segments, temps_trapeze_numpy, color='blue',label='trapèze numpy')
    plt.plot(segments, temps_rectangle_math, color= 'yellow',label='rectangle math')
    plt.plot(segments, temps_rectangle_numpy, color='green',label='rectangle numpy')
    plt.plot(segments, temps_simpson_math, color='orange',label='simpson math')
    plt.plot(segments, temps_simpson_numpy, color='red',label='simpson numpy')
    plt.plot(segments, temps_simpson_scipy, color='pink',label='simpson scipy')
    plt.xlabel('nombre de segments')
    plt.ylabel("temps d'excution (s)")
    plt.yscale('log')
    plt.title('temps en fonction de nombre de segments')
    plt.legend()
    plt.grid(True)


    #graph convergence en fonction du nombre de segments
    plt.figure(figsize=(10,6))
    plt.plot(segments,res_trapeze_math )
    plt.plot(segments, res_trapeze_math, color='c', label='trapèze math')
    plt.plot(segments, res_trapeze_numpy, color='blue', label='trapèze numpy')
    plt.plot(segments, res_rectangle_math, color='yellow', label='rectangle math')
    plt.plot(segments, res_rectangle_numpy, color='green', label='rectangle numpy')
    plt.plot(segments, res_simpson_math, color='orange', label='simpson math')
    plt.plot(segments, res_simpson_numpy, color='red', label='simpson numpy')
    plt.plot(segments, res_simpson_scipy, color='pink', label='simpson scipy')
    plt.xlabel('nombre de segments')
    plt.ylabel("résultats")
    plt.title('Résultats des différentes méthodes en fonction du nombre de segments')
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()