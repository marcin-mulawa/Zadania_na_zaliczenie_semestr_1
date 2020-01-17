import matplotlib.pyplot as plt


def f_line(a, b):
    x = [i for i in range(-100, 100)]
    y = [a*i+b for i in x]
    return x, y


for i in range(10):
    plt.figure()
    x, y = f_line(i, 2*i)
    plt.plot(x, y)
    plt.savefig("wykres_{}_do_zadania_18.png".format(i))
