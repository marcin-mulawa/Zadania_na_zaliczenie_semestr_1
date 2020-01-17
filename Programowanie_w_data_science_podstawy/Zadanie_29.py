def korelacja(x, y):
    x2 = []
    y2 = []
    listy = []
    for i in range(len(x)):
        listy.append(x[i]*y[i])
        x2.append(x[i]**2)
        y2.append(y[i]**2)
    licznik = len(x)*sum(listy)-sum(x)*sum(y)
    mianownik = ((len(x)*sum(x2)-(sum(x))**2) * (len(x)*sum(y2)-(sum(y)**2)))**0.5
    return licznik / mianownik


lista1 = [i for i in range(5)]
lista2=[3,7,9,2,1]

kor = korelacja(lista1, lista2)
print(kor)