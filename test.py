import random
import time
import numpy as np
#Generate 5 random numbers between 10 and 30
n=2000
start = 3
s = time.perf_counter()
randomlist = random.sample(range(0, n), n)
idx = randomlist.index(start)
randomlist[0], randomlist[idx] = randomlist[idx], randomlist[0]
e = time.perf_counter()
print("Time generate by random: ",e - s)

s = time.perf_counter()
listPoint = list(range(n)) # node
tmp = listPoint[0] #swap
listPoint[0] = listPoint[start]
listPoint[start] = tmp
permute = listPoint[1:].copy() #permutation the list point
permuted = list(np.random.permutation(permute))
permuted.insert(0, listPoint[0])
listPoint = permuted
e = time.perf_counter()
print("Time permutation: ",e - s)


#print(listPoint)