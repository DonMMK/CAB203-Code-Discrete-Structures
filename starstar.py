def sum(*values):
    s = 0
    for v in values:
        s = s + v
    return s

s = sum(1, 2, 3, 4, 5)
