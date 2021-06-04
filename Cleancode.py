# Test data has the dictionary with no spaces for the strings
# Declare start and end for specific instance.
testData = (
        {
        ("Time", "Set") : "Timezone2",
        ("Timezone2","Set" ) : "Time",
        ("Time","LongPressSet" ) : "TimeSet",
        ("TimeSet","Set" ) : "Time",
        ("TimeSet", "LongPressSet" ) : "DateSet",
        ("DateSet","Set" ) : "TimeSet",
        ("Time", "Mode") : "Timer",
        ("Timer", "Set") : "TimerSet",
        ("TimerSet","Set" ) : "Timer",
        ("Timer", "Mode") : "Stopwatch",
        ("Stopwatch", "Mode") : "Alarm1",
        ("Alarm1", "LongPressSet") : "Alarm1Set",
        ("Alarm1Set", "Set") : "Alarm1",
        ("Alarm1", "Mode") : "Alarm2",
        ("Alarm2", "Set" ) : "Alarm2Set",
        ("Alarm2Set", "LongPressSet") : "Alarm2",
        ("Alarm2", "Mode") : "Time",
         } ,
        "Time", # This is the start state
        "DateSet") # This is the end state
# When changing the testdata ensure that state has the same format as the dictionary
    
# Edges
# Declaring it as a set so it can be used later
E = set()
for (u,v) in testData[0].keys():
    E.add((u, testData[0][(u,v)]))

# Vertices
# Declaring it as a set so it can be used later
V = set()
for  u in testData[0].values():
    V.add(u)

foundList = []    
    
# Cite: Code from graphs.py extra matertial
def N(V, E, u):
    return { v for v in V if (u,v) in E }    

# Cite: Code from graphs.py extra matertial
# Given below is the depth first function but renamed to fit the CRA
def depthFirst(V, E, u):
    T = {u}  # set of vertices already seen
    depthFirstR(V, E, u, T)
    return T

def depthFirstR(V, E, u, T):
    global foundList
    foundList.append(u)
    if len(T) == len(V) or testData[2] in T: 
        return T # already seen all?

    Nu = N(V, E, u) - T     # Neighbours not already seen
    T.update(Nu)            # Update set of vertices seen
    for v in Nu:
        T.update(depthFirstR(V, E, v, T))  # update vertices seen in branch
    return T

depthFirst(V, E, testData[1])
stateSequence = foundList[0:foundList.index(testData[2]) + 1]
print('The state changes are',stateSequence)

buttons = []
for i in range(len(stateSequence) - 1):
    for (u,v) in testData[0].keys():
        if u == stateSequence[i] and testData[0][(u,v)] == stateSequence[i + 1]:
            buttons.append(v)

print('The buttons that should be pressed are',buttons)