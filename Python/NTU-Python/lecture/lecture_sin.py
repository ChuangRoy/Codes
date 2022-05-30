from matplotlib import pyplot as plt
from lecture_utils import sin_example


start = -3
end = 3
f= 528

x, y = sin_example(start, end, f)

plt.plot(x, y)
plt.vlines(0, 1.5, -1.5, color="red")
plt.vlines(1, 1.5, -1.5, color="red")
plt.grid()
plt.show()
