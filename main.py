import time
import numpy as np
import discrete

"""
NOTE: it's not the get identity that's taking forever,
it's creating the U array!
Also, when N gets too large, the size of the array is the limit,
not the speed of getting identity
"""

N = 10000

def op(a: str, b: str):
    return a + b

u = ["bah"*(N-1-i) for i in range(N)]

system = discrete.AlgebraicSystem(u, [op])

print("system made")

t1 = time.time()
print(system.get_identity())
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(system.get_identity())
t2 = time.time()
print(t2-t1)

"""
n = 100_000

Z_n = range(n)

def plus_mod_n(lop: int, rop: int):
    global n
    return (lop + rop) % n

system = discrete.AlgebraicSystem(Z_n, [plus_mod_n])

t1 = time.time()
print(system.get_identity())
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(system.get_identity())
t2 = time.time()
print(t2-t1)
"""
