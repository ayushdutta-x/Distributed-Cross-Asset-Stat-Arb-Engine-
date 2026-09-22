'''visualising the evolution of the price levels two synthetic non-stationary assets over time.'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 2000
epsz = np.random.normal(0,1,n)
epsa = np.random.normal(0,0.5,n)
epsb = np.random.normal(0,0.5,n)

z = np.cumsum(epsz)
a = z + epsa
b = 2*z + epsb

plt.plot(a, label = 'a')
plt.plot(b, label = 'b')
plt.xlabel("time")
plt.ylabel("price(z)")
plt.title("two non-stationary assets")
plt.legend()
plt.show()