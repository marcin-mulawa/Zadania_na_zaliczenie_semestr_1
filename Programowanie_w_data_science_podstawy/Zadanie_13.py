def silnia(n):
    silnia=1
    for i in range(1,n+1):
        silnia*=i
    return silnia


def newton(n, k):
    return silnia(n) / (silnia(k) * silnia(n-k))


n = int(input("Podaj n: "))
k = int(input("Podaj k: "))
print(newton(n, k))
