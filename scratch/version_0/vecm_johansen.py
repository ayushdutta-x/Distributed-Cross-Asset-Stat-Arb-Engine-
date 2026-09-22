'''interpreting the results of the Johansen cointegrationg test on a known synthetic cointegration relationship'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.vecm import coint_johansen

np.random.seed(42)
n = 20000

espz1 = np.random.normal(0,1,n)
espz2 = np.random.normal(0,1,n)

Z1 = np.cumsum(espz1)

espa = np.random.normal(0,0.5,n)
espb = np.random.normal(0,0.5,n)
espc = np.random.normal(0,0.5,n)

A = Z1 + espa
B = 2*Z1 + espb
C = 3*Z1 + espc

X = pd.DataFrame({
        "A":A,
        "B":B,
        "C":C
})

spreads = pd.DataFrame({
        "B-2A":B-2*A,
        "C-3A":C-3*A
})

result = coint_johansen(
        X,
        det_order = 0,   
        k_ar_diff = 1    #I(n) -- what is n
)

# printing the eigenvalues
print("Eigenvalues")
print(result.eig)

#printing the trace statistics and cvs for confidence intervals (90, 95, 99)
print("Trace statistics")
print(result.lr1)
print("Critical values:")
print(result.cvt)

# finally printing the cointegration vectors 
# build the spanning space as linear combination of all these cointegration vectors
print("vector results")
print(result.evec)