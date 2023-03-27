import types
import numpy as np

class AlgebraicSystem:

    """
    Class to represent an algebraic system.
    System must have a finite universe.
    """

    def __init__(
            self,
            universe: np.ndarray,
            operations: np.ndarray[types.FunctionType]
            ):
        self.__op = np.array(operations)
        self.__num_op = self.__op.shape[0] - 1
        self.__u = np.unique(universe)
        self.__associative = None

    
    def is_associative(self):
        """
        return 1 if associative, else 0
        TODO: address memory complexity shape=(n, n, n, 3) not (n, 3)?
        """
        if self.__associative is not None:
            return self.__associative
        product = cartesian_product(
                self.__u, self.__u, self.__u)
        for (a,b,c) in product:
            if self.operation(
                    self.operation(a,b), c) != self.operation(
                            a, self.operation(b,c)):
                self.__associative = 0
                return 0
        self.__associative = 1
        return 1


    def operation(self, lop, rop, idx=0):
        """
        perform binary operation as lop * rop
        """
        if (lop not in self.__u) or (rop not in self.__u):
            raise Exception("invalid operation: operand(s) not in universe")
        self.__check_op_idx(idx)
        return self.__op[idx](lop, rop)


    def operation_table_to_csv(
            self, file_path, op_idx=0, op_name="operation"):
        """
        write operation[op_idx] to csv at file_path
        """
        with open(file_path, "w") as fp:
            header = ", ".join([op_name] + [f"{i}" for i in self.__u])
            fp.write(header + "\n")

            for a in self.__u:
                row = ", ".join([str(a)] 
                        + [f"{self.operation(a,b)}" for b in self.__u])
                fp.write(row + "\n")


    def __check_op_idx(self, idx):
        if idx > self.__num_op:
            raise Exception(f"idx={idx} outside of operation array bounds")


    def __check_op(self, op):
        if op not in self.__u:
            raise Exception(
                    f"invalid operation: operand '{op}' not in universe")



def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)
