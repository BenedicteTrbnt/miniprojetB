import numpy as np
import matplotlib.pyplot as plt
import fonction_trapeze as tr
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
            n = int(input("entrez le nombre de trapèzes :"))
            break
        except ValueError:
            print("entrez un entier")

    #calcul des intégrales et temps:
    resultat_math, temps_math, resultat_numpy, temps_numpy = tr.mesurer_temps_integral(a,b,n,p1,p2,p3,p4,fonction)
    print(f"résultat avec numpy : {resultat_numpy}, temps d'exécution : {temps_numpy:.6f} secondes") #temps en sec avec 6 chiffres apres virgule
    print(f"résultat avec math : {resultat_math}, temps d'exécution : {temps_math:.6f} secondes")

    Iexact = integrale_exacte(a,b,p1,p2,p3,p4)
    print(f"Solution exacte : {Iexact}")

    #donnée pour les graphes :
    segments = np.arange(10, 1000, 10)
    erreur_trapeze_math = []
    erreur_trapeze_numpy = []
    temps_trapeze_math = []
    temps_trapeze_numpy = []

    for n in segments:
        resultat_math, temps_math, resultat_numpy, temps_numpy = tr.mesurer_temps_integral(a,b,n,p1,p2,p3,p4,fonction)
        temps_trapeze_math.append(temps_math)
        erreur_trapeze_math.append(abs(resultat_math - Iexact))
        temps_trapeze_numpy.append(temps_numpy)
        erreur_trapeze_numpy.append(abs(resultat_numpy - Iexact))
    # ggraph de convergence
    plt.figure(figsize=(10, 6))
    plt.plot(segments, erreur_trapeze_math, label='trapèze math')
    plt.plot(segments, erreur_trapeze_numpy, label='trapèze numy')
    plt.xlabel('nombre des segments')
    plt.ylabel("l'erreur")
    plt.yscale('log')
    plt.title('convergence')
    plt.legend()
    plt.grid(True)

    #graph du temps d'excution
    plt.figure(figsize=(10, 6))
    plt.plot(segments, temps_trapeze_math, label='trapèze math')
    plt.plot(segments, temps_trapeze_numpy, label='trapèze numpy')
    plt.xlabel('nombre de segments')
    plt.ylabel("temps d'excution (s)")
    plt.yscale('log')
    plt.title('temps en fonction de nombre de segments')
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()