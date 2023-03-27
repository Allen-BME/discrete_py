import time
import numpy as np
import discrete

n = 100

Z_n = range(n)

def plus_mod_n(lop: int, rop: int):
    global n
    return (lop + rop) % n

system = discrete.AlgebraicSystem(Z_n, [plus_mod_n])

t1 = time.time()
print(system.is_associative())
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(system.is_associative())
t2 = time.time()
print(t2-t1)

