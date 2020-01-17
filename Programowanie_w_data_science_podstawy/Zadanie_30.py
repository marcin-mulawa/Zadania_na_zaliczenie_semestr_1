import numpy as np
from collections import Counter
import matplotlib.pyplot as plt



def average(lista):
    average = 0
    for el in lista:
        average+=el
    average = average / len(lista)
    return average


def mediana(lista):
    length = len(lista)
    lista.sort()
    if length %2==0:
        suma = lista[int(length/2-1)]+ lista[int(length/2)]
        return suma/2
    return lista[int(length//2+1)-1]


def moda(lista):
    return Counter(lista).most_common(1)


def std(lista):
    avg = np.mean(lista)
    return(sum((lista - avg)**2)/len(lista))**0.5
 
    
def var(lista):
    avg = np.mean(lista)
    return sum((lista - avg)**2)/len(lista)


def skosnosc(lista):
    avg=np.mean(lista)
    return 1/len(lista)*sum((lista-avg)**3)/(np.std(lista))**3


def kurtoza(lista):
    avg = np.mean(lista)
    return 1/len(lista)*sum((lista-avg)**4)/(np.std(lista))**4 -3


liczby = np.random.normal(size=1000)
plt.hist(liczby, bins=12)
print('Srednia wynosi {}'.format(average(liczby)))
print('Mediana wynosi {}'.format(mediana(liczby)))
print('Dominanta wynosi {}'.format(moda(liczby)))
print('Odchylenie standardowe wynosi {}'.format(std(liczby)))
print('Wariancja wynosi {}'.format(var(liczby)))
print('Skosnosc wynosi {}'.format(skosnosc(liczby)))
print('Kurtoza wynosi {}'.format(kurtoza(liczby)))