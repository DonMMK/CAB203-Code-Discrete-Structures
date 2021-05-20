def isBiPartite(V, E):
    Vertices = (V & E ==set() )
    Condition =(V | E == V.union(E)) 
    if ( Vertices & Condition):
        return True
    return False
