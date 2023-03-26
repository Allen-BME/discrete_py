import types

class AlgebraicSystem:

    def __init__(self, universe: set, operation: types.FunctionType):
        self.__op = operation
        self.__u = universe

    def operation(self, lop, rop):
        if (lop not in self.__u) or (rop not in self.__u):
            raise Exception("invalid operation: operand(s) not in universe")
        return self.__op(lop, rop)


if __name__ == "__main__":

    my_universe = {0, 1, 2, 3}

    def my_binary_op(lop: int, rop: int):
        return (lop + rop) % 4

    system = AlgebraicSystem(my_universe, my_binary_op)
    
    for a in my_universe:
        print(f"{a} + {a} = {system.operation(a, a)}")
