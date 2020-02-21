#%%
# Monte Carlo
#
 
import numpy as np
 
import random

N=400
delta=1/N

L=[(random.random(), random.random()) for i in range(N) for j in range(N)]

#L = [ (i*delta, j*delta) for i in range(N+1) for j in range(N+1)]
L

count = 0

for k in range(len(L)):
    if ( L[k][0]*L[k][0] + L[k][1]*L[k][1] <= 1 ):
        count += 1
        
4*count/len(L)
