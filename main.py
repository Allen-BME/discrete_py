import discrete

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


print("------------------------------")

n = get_input()

Z_n = range(n)

def plus_mod_n(lop: int, rop: int):
    global n
    return (lop + rop) % n

system = discrete.AlgebraicSystem(Z_n, [plus_mod_n])

for a in Z_n:
    print(f"{a} + {a} = {system.operation(a, a)}")

print("------------------------------")



