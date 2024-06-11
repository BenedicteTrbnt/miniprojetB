# Cette version du code calcule la superficie à l'aide des
# 3 méthodes et représente graphiquement les temps de traitement
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def polinomial_tercer_orden(x, a, b, c, d):
    """
    Función que representa un polinomio de tercer orden.

    f(x) = a*x^3 + b*x^2 + c*x + d
    """
    return a * x**3 + b * x**2 + c * x + d

def area_bajo_curva_simpson(a, b, c, d, x_start, x_end, n=1000):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando el método de Simpson.

    a, b, c, d: Coeficientes del polinomio.
    x_start, x_end: Límites de integración.
    n: Número de subintervalos (debe ser par).
    """
    if n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser par.")

    # Anchura de cada subintervalo
    h = (x_end - x_start) / n

    # Sumar los valores de los extremos
    integral = polinomial_tercer_orden(x_start, a, b, c, d) + polinomial_tercer_orden(x_end, a, b, c, d)

    # Sumar los valores de los puntos intermedios
    for i in range(1, n):
        x = x_start + i * h
        if i % 2 == 0:
            integral += 2 * polinomial_tercer_orden(x, a, b, c, d)
        else:
            integral += 4 * polinomial_tercer_orden(x, a, b, c, d)

    # Multiplicar por la anchura de los subintervalos y dividir por 3
    integral *= h / 3

    return integral

def area_bajo_curva_numpy(a, b, c, d, x_start, x_end, n=1000):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando NumPy y el método de Simpson.

    a, b, c, d: Coeficientes del polinomio.
    x_start, x_end: Límites de integración.
    n: Número de puntos.
    """
    # Crear un arreglo de puntos x en el intervalo [x_start, x_end]
    x = np.linspace(x_start, x_end, n)

    # Evaluar el polinomio en cada punto x
    y = a * x**3 + b * x**2 + c * x + d

    # Calcular el área utilizando el método de Simpson
    area = np.trapz(y, x)

    return area

def area_bajo_curva_scipy(a, b, c, d, x_start, x_end, n=1000):
    """
    Calcula el área bajo la curva de una función polinomial de tercer orden
    usando SciPy y el método de Simpson.

    a, b, c, d: Coeficientes del polinomio.
    x_start, x_end: Límites de integración.
    n: Número de puntos.
    """
    # Crear un arreglo de puntos x en el intervalo [x_start, x_end]
    x = np.linspace(x_start, x_end, n)

    # Evaluar el polinomio en cada punto x
    y = a * x**3 + b * x**2 + c * x + d

    # Calcular el área utilizando el método de Simpson de SciPy
    area = simpson(y, x)

    return area

# Parámetros del polinomio y límites de integración
a = 1
b = -2
c = 3
d = -4
x_start = 0
x_end = 2

# Medir el tiempo de ejecución de cada función
time_taken_simpson = timeit.timeit(lambda: area_bajo_curva_simpson(a, b, c, d, x_start, x_end), number=1)
time_taken_numpy = timeit.timeit(lambda: area_bajo_curva_numpy(a, b, c, d, x_start, x_end), number=1)
time_taken_scipy = timeit.timeit(lambda: area_bajo_curva_scipy(a, b, c, d, x_start, x_end), number=1)

# Calcular el área utilizando cada función
area_simpson = area_bajo_curva_simpson(a, b, c, d, x_start, x_end)
area_numpy = area_bajo_curva_numpy(a, b, c, d, x_start, x_end)
area_scipy = area_bajo_curva_scipy(a, b, c, d, x_start, x_end)

# Mostrar los resultados
print(f"El área bajo la curva utilizando el método de Simpson es: {area_simpson}")
print(f"Tiempo de ejecución con el método de Simpson: {time_taken_simpson} segundos")
print(f"El área bajo la curva utilizando NumPy es: {area_numpy}")
print(f"Tiempo de ejecución con NumPy: {time_taken_numpy} segundos")
print(f"El área bajo la curva utilizando SciPy es: {area_scipy}")
print(f"Tiempo de ejecución con SciPy: {time_taken_scipy} segundos")

# Graficar los tiempos de ejecución
methods = ['Simpson', 'NumPy', 'SciPy']
times = [time_taken_simpson, time_taken_numpy, time_taken_scipy]

plt.figure(figsize=(10, 6))
plt.bar(methods, times, color=['blue', 'green', 'red'])
plt.xlabel('Método')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución')
plt.show()
