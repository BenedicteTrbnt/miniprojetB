# variables fixées pour créer la méthode (à supprimer et demander à l'utlisateur de les choisir dans le main)
x_start=0
x_end=2
n=100
a = 1
b = -2
c = 3
d = -4

# import
import timeit
import numpy as np
import matplotlib.pyplot as plt

def polinomial_tercer_orden(x, a, b, c, d):
    return (a * x**3) + (b * x**2) + (c * x) + d

def area_rectangle(a, b, c, d, x_start, x_end, n):
    l = (x_end - x_start)/n
    integrale_rect = 0
    for i in range(1,n):
        x= x_start + (i*l)
        integrale_rect += l * polinomial_tercer_orden(x + (l/2),a,b,c,d)
    return (integrale_rect)

def area_rectangle_numpy(a, b, c, d, x_start, x_end, n):
    x = np.linspace(x_start, x_end, n)
    integrale_rect_numpy = 0
    for j in range(0, len(x) - 1):
        integrale_rect_numpy += (x[j+1]-x[j]) * polinomial_tercer_orden(x[j + 1] + (x[j] / 2),a,b,c,d)
    return (integrale_rect_numpy)

# calcul de l'erreur entre les deux méthodes
def erreur(a, b, c, d, x_start, x_end, n):
    err= area_rectangle_numpy(a, b, c, d, x_start, x_end, n) - area_rectangle(a, b, c, d, x_start, x_end, n)
    return(err)

# timer pour 1000 itérations
time_taken_rect1000 = timeit.timeit(lambda: area_rectangle(a, b, c, d, x_start, x_end,n), number=1000)
time_taken_rect_numpy1000 = timeit.timeit(lambda: area_rectangle_numpy(a, b, c, d, x_start, x_end,n), number=1000)

# timer pour 10000 itérations
time_taken_rect10000 = timeit.timeit(lambda: area_rectangle(a, b, c, d, x_start, x_end,n), number=10000)
time_taken_rect_numpy10000 = timeit.timeit(lambda: area_rectangle_numpy(a, b, c, d, x_start, x_end,n), number=10000)

# affichage des valeurs et des timers
print(f"L'air sous la courbe d'après la méthode des rectangles : ", area_rectangle(a, b, c, d, x_start, x_end, n))
print(f"Le temps pour 1000 itérations : ", time_taken_rect1000)
print(f"L'air sous la courbe d'après la méthode des rectangles : ", area_rectangle_numpy(a, b, c, d, x_start, x_end, n))
print(f"Le temps pour 1000 itérations : ", time_taken_rect_numpy1000)
print(f"L'erreur entre la méthode des rectangles en python et celle en numpy est : ", erreur(a, b, c, d, x_start, x_end, n))

# graphiques pour le rapport

# afficage de la courbe et des rectangles
x = np.linspace(x_start,x_end,n)
y=polinomial_tercer_orden(x, a, b, c, d)
for i in range(n-1):
    x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
    y_rect = [0, y[i], y[i], 0, 0] # ordonnees des sommets
    plt.plot(x_rect, y_rect,"r")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Courbe du polynôme + représentation de la méthode des rectangles')
plt.plot(x,y)
plt.grid()
plt.plot()
plt.show()

# graphiques comparaison des temps d'éxecution pour la méthodes des rectangles
methods = ['Python rectangle', 'NumPy rectangle', 'Python rectangle', 'NumPy rectangle']
times= [time_taken_rect1000, time_taken_rect_numpy1000, time_taken_rect10000, time_taken_rect_numpy10000]
plt.bar(methods, times, color=['blue', 'red', 'blue','red'])
plt.xlabel('Méthodes')
plt.ylabel('Temps d\'éxécution pour 1000 itérations en bleu, pour 10000 itérations en rouge (en s)')
plt.title('Comparaison des temps d\'éxécution en fonction des méthodes et du nombre d\'itérations')
plt.grid()
plt.show()

# graphique montrant la convergence en fonction du nombre de segments pour toutes les méthodes
#
segments=[10,50, 80,100,200, 300, 400, 500, 600, 700, 800, 100, 1000]

for i in range(len(segments)):
    y_1=area_rectangle(a, b, c, d, x_start, x_end, segments[i])
    y_2=area_rectangle_numpy(a, b, c, d, x_start, x_end, segments[i])
    plt.plot(segments[i],y_1,'o', color='blue')
    plt.plot(segments[i],y_2,'o',color='red')
plt.xlabel('Nombre de segments')
plt.ylabel('Aire sous la courbe')
plt.title('Aire sous la courbe en fonction du nombre de segments, en bleu la méthode des rectangles Python, en rouge Numpy')
plt.grid()
plt.show()



# graphique montrant l’erreur en fonction de la méthode utilisée et du nombre de segments
segments=[10,50, 80,100,200, 300, 400, 500, 600, 700, 800, 100, 1000]

for i in range(len(segments)):
    y_3=erreur(a, b, c, d, x_start, x_end, segments[i])
    plt.plot(segments[i],y_3,'o', color='c')
plt.xlabel('Nombre de segments')
plt.ylabel('Erreur entre les méthodes des rectangles Python et Numpy')
plt.title('L\'erreur en fonction du nombre de segments pour la méthode des rectangles')
plt.grid()
plt.show()