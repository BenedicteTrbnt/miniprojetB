# Cette version du code calcule la superficie à l'aide des
# 3 méthodes et représente graphiquement les temps de traitement
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def area_bajo_curva_simpson(p1, p2, p3, p4, a, b, n,fonction):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando el método de Simpson.

    p1, p2, p3, p4: Coeficientes del polinomio.
    a, b : Límites de integración.
    n: Número de subintervalos (debe ser par).
    """
    if n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser par.")

    # Anchura de cada subintervalo
    h = (b - a) / n

    # Sumar los valores de los extremos
    integral = fonction(a, p1, p2, p3, p4) + fonction(b, p1, p2, p3, p4)

    # Sumar los valores de los puntos intermedios
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * fonction(x, p1, p2, p3, p4)
        else:
            integral += 4 * fonction(x, p1, p2, p3, p4)

    # Multiplicar por la anchura de los subintervalos y dividir por 3
    integral *= h / 3

    return integral

def area_bajo_curva_numpy(p1, p2, p3, p4, a, b, n):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando NumPy y el método de Simpson.

    p1, p2, p3, p4 : Coeficientes del polinomio.
    a, b: Límites de integración.
    n: Número de puntos.
    """
    # Crear un arreglo de puntos x en el intervalo [x_start, x_end]
    x = np.linspace(a, b, n+1)

    # Evaluar el polinomio en cada punto x
    y = p1+ p2*x + p3* x**2 + p4 * x**3

    # Calcular el área utilizando el método de Simpson
    area = np.trapz(y, x)

    return area

def area_bajo_curva_scipy(p1, p2, p3, p4, a, b, n):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando SciPy y el método de Simpson.

    p1, p2, p3, p4: Coeficientes del polinomio.
    a, b: Límites de integración.
    n: Número de puntos.
    """
    # Crear un arreglo de puntos x en el intervalo [x_start, x_end]
    x = np.linspace(a, b, n+1)

    # Evaluar el polinomio en cada punto x
    y = p1+ p2*x + p3* x**2 + p4 * x**3

    # Calcular el área utilizando el método de Simpson de SciPy
    area = simpson(y, x)

    return area
def mesurer_temps_simpson(a,b,n,p1,p2,p3,p4,fonction): #calcul de temps d'excution
    temps_math_simpson = timeit.timeit(lambda: area_bajo_curva_simpson(p1,p2,p3,p4,a,b,n,fonction), number=100000)
    resultat_math_simpson = area_bajo_curva_simpson(p1,p2,p3,p4,a,b,n,fonction)
    temps_numpy_simpson = timeit.timeit(lambda: area_bajo_curva_numpy(p1,p2,p3,p4,a,b,n), number=100000)
    resultat_numpy_simpson = area_bajo_curva_numpy(p1,p2,p3,p4,a,b,n)
    temps_scipy_simpson = timeit.timeit(lambda:area_bajo_curva_scipy(p1, p2, p3, p4, a, b, n),number=100000)
    resultat_scipy_simpson = area_bajo_curva_scipy(p1, p2, p3, p4, a, b, n)
    return resultat_math_simpson, temps_math_simpson, resultat_numpy_simpson, temps_numpy_simpson, temps_scipy_simpson, resultat_scipy_simpson









# Mostrar los resultados
#print(f"El área bajo la curva utilizando el método de Simpson es: {area_simpson}")
#print(f"Tiempo de ejecución con el método de Simpson: {time_taken_simpson} segundos")
#print(f"El área bajo la curva utilizando NumPy es: {area_numpy}")
#print(f"Tiempo de ejecución con NumPy: {time_taken_numpy} segundos")
#print(f"El área bajo la curva utilizando SciPy es: {area_scipy}")
#print(f"Tiempo de ejecución con SciPy: {time_taken_scipy} segundos")

# Graficar los tiempos de ejecución
#methods = ['Simpson', 'NumPy', 'SciPy']
#times = [time_taken_simpson, time_taken_numpy, time_taken_scipy]

#plt.figure(figsize=(10, 6))
#plt.bar(methods, times, color=['blue', 'green', 'red'])
#plt.xlabel('Método')
#plt.ylabel('Tiempo de ejecución (segundos)')
#plt.title('Comparación de tiempos de ejecución')
#plt.show()