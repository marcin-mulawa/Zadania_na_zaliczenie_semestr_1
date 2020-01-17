def silnia_iter(n):
    silnia=1
    for i in range(1, n+1):
        silnia *= i
    return silnia


def silnia_rec(n):
    if n == 0 or n == 1:
        return 1
    return n*silnia_rec(n-1)


dec = 't'
while dec == 't':
    n = int(input("podaj liczbę, dla której chcesz policzyć silnię: "))
    print(silnia_iter(n))
    print(silnia_rec(n))
    dec=input('Czy chcesz policzyć dla kolejnej liczby? t/n: ')