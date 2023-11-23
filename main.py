# Equation x2

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-50, 60, 100)
y = x ** 2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Courbe d'équation y = x²")
plt.show()