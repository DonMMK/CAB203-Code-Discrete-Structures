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
         } , "Time" , "DateSet" )
# When changing the testdata ensure that state has the same format as the dictionary


graph = {
    'Time' : ['Timezone2','TimeSet' , 'Timer'],
    'TimeSet' : ['DateSet', 'Time'],
    'Timezone2' : ['Time'],
    'DateSet' : ['TimeSet'],
    'Timer' : ['TimerSet' , 'Stopwatch'],
    'TimerSet' : ['Timer'],
    'Stopwatch' : ['Alarm1'],
    'Alarm1' : ['Alarm1Set' , 'Alarm2'],
    'Alarm1Set' : ['Alarm1'],
    'Alarm2' : ['Alarm2Set' , 'Time'],
    'Alarm2Set' : ['Alarm2']
}

#visited = set() # Set to keep track of visited nodes.

#def dfs(visited, graph, node):
#    if node not in visited:
#        print (node)
#        visited.add(node)
#        for neighbour in graph[node]:
#            dfs(visited, graph, neighbour)

# Driver Code
#dfs(visited, graph, 'Time') # assume started at Time



#def runFSA(start, testData , accepting, input) :
#    state = start   
#    for i in input :
#        state  = testData[ (state , i)]
#        if state in accepting:
#            return True
#        return False
    
   
# Code to get neighbourhoods   
    
# Cite: Code from graphs.py extra matertial
# Input Vertex , Edge , visited
E = set()
for (u,v) in testData[0].keys():
    E.add((u, testData[0][(u,v)]))


V = set()
for  u in testData[0].values():
    V.add(u)

foundList = []    
    
def N(V, E, u):
    return { v for v in V if (u,v) in E }    

def depthFirst(V, E, u):
    T = {u}             # set of vertices already seen
    depthFirstR(V, E, u, T)
    return T

def depthFirstR(V, E, u, T):
    global foundList
    foundList.append(u)
    #print('processing ', u)                # process vertex u
    if len(T) == len(V) or testData[2] in T: 
        return T # already seen all?

    Nu = N(V, E, u) - T     # Neighbours not already seen
    T.update(Nu)            # Update set of vertices seen
    for v in Nu:
        T.update(depthFirstR(V, E, v, T))  # update vertices seen in branch
    return T


print()

depthFirst(V, E, testData[1])
stateSequence = foundList[0:foundList.index(testData[2]) + 1]
print(stateSequence)

buttons = []
for i in range(len(stateSequence) - 1):
    for (u,v) in testData[0].keys():
        if u == stateSequence[i] and testData[0][(u,v)] == stateSequence[i + 1]:
            buttons.append(v)

print(buttons)