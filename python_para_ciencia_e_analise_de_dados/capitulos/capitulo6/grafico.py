import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 5))
plt.title("Função de segundo grau")

x = np.linspace(-10, 10, 1000)
y = x ** 3 + 10 * x ** 2 + 5 * x

plt.plot(x, y)
plt.show()
