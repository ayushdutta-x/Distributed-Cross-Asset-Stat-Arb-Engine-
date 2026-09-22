'''stationarity and the Augmented-Dickey-Fuller (ADF) Test'''

from statsmodels.tsa.stattools import adfuller
import numpy as np

n=2000
epsz = np.random.normal (0,1,n)
z = np.cumsum(epsz)

epsa = np.random.normal(0,0.5,n)
epsb = np.random.normal(0,0.5,n)

a = z + epsa
b = 2*z + epsb
spread = b-2*a

result_A = adfuller(a)
result_spread = adfuller(spread)
print("A:")
print("ADF statistic:", result_A[0])
print("p-value:", result_A[1])

print("\nSpread:")
print("ADF statistic:", result_spread[0])
print("p-value:", result_spread[1])



# visualising the spread as a stationary time series
chunks = np.array_split(spread, 4)

for i, chunk in enumerate(chunks):
    print(
        f"Chunk {i+1}: "
        f"mean={np.mean(chunk):.3f}, "
        f"std={np.std(chunk):.3f}"
    )

plt.hist(spread,bins=50,alpha = 0.7,density = True)
plt.xlabel("Time")
plt.ylabel("Spread")
plt.show()