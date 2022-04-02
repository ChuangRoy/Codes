from matplotlib import pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [-1, 4, -3, 6, 8]

x2 = [1, 2, 3, 4, 5]
y2 = [23, 45, 3, 1, 5]

# plt.subplot(row, col, idx)
plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title("funcion 1")

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r')
plt.title("funcion 2")

plt.tight_layout()
plt.show()

