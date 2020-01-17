def fib_iter(n):
    f=0
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for i in range(2, n+1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f


def fib_rec(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


n = int(input("Podaj, który element ciągu fibonacciego chcesz obliczyć: "))
print(fib_rec(n))
print(fib_iter(n))
