# Program plots use NumPy and MatplotLib to create a graph: y = x^2
import matplotlib.pyplot as plt
import numpy as np

def squaredValues(x):
    return x*x

data = np.arange(100)

"""
for i in range(100):
    output = squaredValues(i)
    data.append(output)
"""
print(data)

plt.plot(squaredValues(data))
plt.show()