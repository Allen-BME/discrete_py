import numpy as np
import discrete

n = 13

Z_13 = range(13)

def plus_mod_13(lop: int, rop: int):
    return (lop + rop) % 13

system = discrete.AlgebraicSystem(Z_13, [plus_mod_13])

system.operation_table_to_csv("test.csv", op_name="+_13")
