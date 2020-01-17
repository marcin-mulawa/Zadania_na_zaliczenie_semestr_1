import numpy as np

n = int(input('Podaj stopien macierzy: '))
A = []
for i in range(n*n):
    A.append(np.random.choice([0,255]))
    
A = np.asarray(A).reshape(n,n)