def logicallyImplies(A, B):

    p = True
    q = False
    AtruthValue = A(p , q)
    BtruthValue = B(p , q)
    if (AtruthValue & ~BtruthValue):
        return False
    else:
        return True 

        
