#/usr/bin/python3
delta ={(1, 0) : 2,
        (1, 1) : 1,
        (2, 0) : 2,
        (2, 1) : 3,
        (3, 0) : 2,
        (3, 1) : 3 }

def runFSA(start, delta , accepting, input) :
    state = start   
    for i in input :
        state  = delta[ (state , i)]
        if state in accepting:
            return True
        return False
    
print(runFSA(1, delta , {3} , (1,0,0)))
    
