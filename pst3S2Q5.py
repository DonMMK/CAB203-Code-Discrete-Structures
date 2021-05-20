def GED(x, y):
    if x % y == 0:
        return y
    else:
        z = x % y
        GED(y, z)
        return z
