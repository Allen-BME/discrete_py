import itertools
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
        self.__check_closure()
        self.__associative = None
        self.__e = None
        self.__checked_e = False

    
    def is_associative(self):
        """
        return True if associative, else False.
        WARNING: takes really really long as |U| increases
        """
        if self.__associative is not None:
            return self.__associative
        for (a,b,c) in itertools.product(
                self.__u, self.__u, self.__u):
            if self.operation(
                    self.operation(a,b), c) != self.operation(
                            a, self.operation(b,c)):
                self.__associative = False
                return False
        self.__associative = True
        return True


    def get_identity(self, op_idx=0):
        """
        return identity element for op[op_idx] if there is one, else None
        """
        if (self.__checked_e) and (self.__e is None):
            return self.__e
        self.__checked_e = True
        for e in self.__u:
            e_is_identity = True
            for a in self.__u:
                if ((self.__op[op_idx](a, e) != self.__op[op_idx](e, a)) or
                        self.__op[op_idx](a, e) != a):
                    e_is_identity = False
                    break
            if e_is_identity:
                self.__e = e
                return e
                    

    def get_inverse(self, a, op_idx=0):
        """
        return a^-1 for a if it exists in op[op_idx], else None.

        Note: I'm not sure if there are systems where a might have more
        than 1 inverse, so this just returns the first inverse it finds
        """
        # first, there needs to be an identity
        if not (self.__checked_e):
            self.get_identity()
        if (self.__e is None):
            return None  # if no identity, no element has an inverse

        # find inverse
        for a_inv in self.__u:
            if self.operation(
                    a, a_inv, op_idx=op_idx) == self.__e:
                return a_inv
        return None


    def operation(self, lop, rop, idx=0):
        """
        perform binary operation as lop * rop
        """
        self.__check_op(lop)
        self.__check_op(rop)
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


    def __check_closure(self):
        for op_idx in range(self.__num_op):
            for (a,b) in itertools.product(self.__u, self.__u):
                if self.operation(a, b, op_idx=i) not in self.__u:
                    raise Exception(f"system")


    def __check_op_idx(self, idx):
        if idx > self.__num_op:
            raise Exception(f"idx={idx} outside of operation array bounds")


    def __check_op(self, op):
        if op not in self.__u:
            raise Exception(
                    f"invalid operation: operand '{op}' not in universe")



class Z_n:

    """
    Class implementation of Group Z_n equipped with operation plus_mod_n.
    """

    def __init__(self, n):
        self.n = n
        self.__u = np.arange(n)


    def elements(self):
        return self.__u


    def plus_mod_n(self, lop, rop):
        self.__check_op(lop)
        self.__check_op(rop)
        return (lop + rop) % self.n

    
    def operation(self, lop, rop):
        """
        alias for plus_mod_n (for consistency with AlgebraicStructure)
        """
        self.__check_op(lop)
        self.__check_op(rop)
        return (lop + rop) % self.n


    def is_associative(self):
        return True


    def get_inverse(self, a):
        self.__check_op(a)
        return (self.n - a) % n


    def get_identity(self):
        return 0


    def operation_table_to_csv(self, file_path):
        """
        write plus_mod_n to csv at file_path
        """
        with open(file_path, "w") as fp:
            header = ", ".join([f"plus_mod_{self.n}"]
                    + [f"{i}" for i in self.__u])
            fp.write(header + "\n")

            for a in self.__u:
                row = ", ".join([str(a)] 
                        + [f"{self.plus_mod_n(a,b)}" for b in self.__u])
                fp.write(row + "\n")


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
