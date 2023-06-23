def cyclic_sub(Z, a):
    sub = set([a])
    b = a
    while b != 0:
        b = (b + a) % Z
        sub.add(b)
    return sub
