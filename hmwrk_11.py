import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi*10, np.pi*10, 500000, endpoint=True)
y =-12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30

ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.plot(x,y)

plt.show()


# **************
# Спасибо за семинары!!!
# *************