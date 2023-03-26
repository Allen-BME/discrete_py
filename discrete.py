import types
import numpy as np

class AlgebraicSystem:


    def __init__(
            self,
            universe: np.ndarray,
            operations: np.ndarray[types.FunctionType]
            ):
        self.__op = np.array(operations)
        self.__num_op = self.__op.shape[0] - 1
        self.__u = np.unique(universe)


    def operation(self, lop, rop, idx=0):
        """
        perform binary operation as lop * rop
        """
        if (lop not in self.__u) or (rop not in self.__u):
            raise Exception("invalid operation: operand(s) not in universe")
        self.__check_op_idx(idx)
        return self.__op[idx](lop, rop)


    def __check_op_idx(self, idx):
        if idx > self.__num_op:
            raise Exception(f"idx={idx} outside of operation array bounds")


    def __check_op(self, op):
        if op not in self.__u:
            raise Exception(
                    f"invalid operation: operand '{op}' not in universe")
