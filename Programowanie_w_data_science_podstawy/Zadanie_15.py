import matplotlib.pyplot as plt


warsaw = [5, 4, 6, 6, 8, 4, 4, 4, 3, 3, 3, 3, 3, 3]
new_york = [5, 9, 2, 6, 14, 13, 13, -1, 7, 15, 17, 17, 9, 5]
miami = [23, 25, 25, 25, 26, 27, 27, 27, 26, 26, 25, 25, 24,  26]

days = [i+1 for i in range(14)]


plt.plot(days, warsaw, 'r+-', markersize=10)
plt.plot(days, new_york, 'bo-', markersize=10)
plt.plot(days, miami, 'yx-', markersize=10)
plt.legend(('Warsaw', 'New York', 'Miami'))
plt.xlabel("Days")
plt.ylabel("Temparatures (℃)")
plt.title('14 days temperatures')
plt.show()