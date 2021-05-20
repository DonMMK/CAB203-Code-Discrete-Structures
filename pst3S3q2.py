def equivClasses( S, R):
    S = frozenset({S})
    R = frozenset({R})
    O = frozenset.intersection(S,R)
    return O
    
