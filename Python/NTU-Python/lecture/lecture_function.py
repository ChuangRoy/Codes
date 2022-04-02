from matplotlib import pyplot as plt

from lecture_utils import samples_example, sample_rate_example

x = [1, 2, 3, 4, 5]
y = [-4, -3, 0, 5, 12]
 
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [32, 21, 12, 5, 0, -3, -4, -3, 0, 5, 12]
 
plt.plot(x, y, '.')
 
start = -20
end = 20
samples = 1000
 
x1, y1 = samples_example(start, end, samples)
 
start = -20
end = 20
fs = 1000
 
x2, y2 = sample_rate_example(start, end, fs)

plt.plot(x2, y2, 'r.')
plt.plot(x1, y1, 'b.')
plt.show()
