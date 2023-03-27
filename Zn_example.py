import time
import discrete
import numpy as np

"""
Generate the operation table for Z_n
where n is chosen by the user
"""


def get_input():
    n = input("Enter an integer >= 2: ")
    while ((not n.isnumeric()) or (int(n) < 2)):
        print("Invalid entry!")
        n = input("Enter an integer >= 2: ")
    return int(n)


# --- user define algebraic system
n = get_input()

Z_n = np.arange(n)

def plus_mod_n(lop: int, rop: int):
    global n
    return (lop + rop) % n

system = discrete.AlgebraicSystem(Z_n, [plus_mod_n])

# --- print 2a for all a in Z

np.vectorize(lambda a: print(f"{a} + {a} = {system.operation(a,a)}"))(Z_n)
