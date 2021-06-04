#!/usr/bin/env python3

testData = (
    {
        ('Brisbane', 'Sydney'),
        ('Vancouver', 'London'),
        ('Paris', 'Brisbane'),
        ('Paris', 'Vancouver'),
        ('Sydney', 'Paris')
    },
    'Brisbane',
    'London'
)

# From graphys.py obtained from CAB203 Blackboard
def N(V, E, u):
    return { v for v in V if (u,v) in E }

# From graphys.py obtained from CAB203 Blackboard
def NS(V, E, S):
    return { v for v in V for u in S if (u,v) in E }

# From graphys.py obtained from CAB203 Blackboard
def arbitraryElement(S):
    return next(iter(S))

# Modified from graphys.py obtained from CAB203 Blackboard
# we now stop when we find the target vertex rather then
# if we run out of vertices or if graph is disconnected.
# Graph is known to be connected so we will always get to target.
def distanceClasses(V, E, u, target):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    if u == target:
        return D
    return distanceClassesR(V0, E, D, target)

# Modified from graphys.py obtained from CAB203 Blackboard
def distanceClassesR(V, E, D, target):
    Vnew = V - D[-1]                          # V_{j} = V_{j-1} / D_{j-1}
    Dnew = D + [ NS(Vnew, E, D[-1]) ]     # D_{j} = N_{V_j}(D_{j-1})
    if target in Dnew[-1]:
        return Dnew
    return distanceClassesR(Vnew, E, Dnew, target)

def solution(instance):
    (L, s, d) = instance
    V = { u for (u,v) in L } | { v for (u,v) in L }
    E = L | { (v,u) for (u,v) in L }
    D = distanceClasses(V, E, d, s)
    j = len(D) - 1  # s will be in the last D
    path = [ s ]
    v = s
    for k in range (j-1, -1, -1):
        v = arbitraryElement(N(D[k],E, v))
        path.append(v)

    return path

def printSolution(solution):
    print('Sequence of cities:')
    for city in solution:
        print(city)
    print('Number of links used:')
    print(len(solution) - 1)

printSolution(solution(testData))
