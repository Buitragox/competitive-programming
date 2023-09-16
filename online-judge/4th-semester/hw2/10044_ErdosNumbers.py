from math import fabs
from sys import stdin
from collections import deque

def bfs(u, adj, visitados, distancia):
    cola = deque()
    cola.append(u)
    visitados[u] = True
    distancia[u] = 0
    while len(cola) != 0:
        v = cola.popleft()
        w = 0
        for i in range(len(adj[v])):
            w = adj[v][i]
            if not visitados[w]:
                cola.append(w)
                visitados[w] = True
                distancia[w] = distancia[v] + 1

def deleteSpaces(name):
    while name[0] == " ":
        name = name[1::]
    while name[-1] == " ":
        name = name[::-1]
    
    return name


def getNames(listNames):
    names = []
    if len(listNames) % 2 != 0:
        del listNames[-1]
    for i in range(0, len(listNames), 2):
        n = deleteSpaces(listNames[i]) + ", " + deleteSpaces(listNames[i + 1])
        names.append(n)
    return names

def main():
    cases = int(input())
    count = 1
    while cases:
        p, n = list(map(int, stdin.readline().split()))
        adj = {}
        for x in range(p):
            listNames = []
            names, title = list(stdin.readline().split(":"))
            listNames = list(names.split(","))
            listNames = getNames(listNames)
            for i in range(len(listNames)):
                if not(listNames[i] in adj):
                    adj[listNames[i]] = []
            
            for i in range(len(listNames)):
                for j in range(len(listNames)):
                    if i != j:
                        if not(listNames[j] in adj[listNames[i]]):
                            adj[listNames[i]].append(listNames[j])

        searched = []
        for y in range(n):
            name = input()
            searched.append(name)
        
        dictKeys = list(adj.keys())
        visitados = {dictKeys[i] : False for i in range(len(adj))}
        distancia = {dictKeys[i] : -1 for i in range(len(adj))}
        if "Erdos, P." in adj:
            bfs("Erdos, P.", adj, visitados, distancia)
        
        print("Scenario", count)
        for s in searched:
            if not(s in distancia):
                print(s, "infinity")
            else:
                dist = distancia[s]
                if dist != -1:
                    print(s, dist)
                else:
                    print(s, "infinity")
        count += 1
        
        cases -= 1

main()