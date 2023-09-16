from sys import stdin

graph = {}
visited = {}
low = {}
father = {}
apNodes = set()
discTime = 0

def apAux(node):
    global discTime, visited, father, low, apNodes
    sons = 0
    discTime += 1
    visited[node] = discTime
    low[node] = discTime
    
    for i in range(len(graph[node])):
        adjNode = graph[node][i]
        if visited[adjNode] == -1:
            sons += 1
            father[adjNode] = node
            apAux(adjNode)
            low[node] = min(low[node], low[adjNode])
            if father[node] != "" and low[adjNode] >= visited[node]:
                apNodes.add(node)
        
        elif adjNode != father[node]:
            low[node] = min(low[node], visited[adjNode])

    if father[node] == "" and sons > 1:
        apNodes.add(node)    

def ap():
    global graph

    keys = list(graph.keys())
    for l in keys:
        if visited[l] == -1:
            apAux(l)    

def main():
    global graph, visited, low, father, apNodes, discTime
    count = 1
    locations = int(input())
    while(locations != 0):
        graph = {}
        visited = {}
        apNodes = set()
        low = {}
        father = {}
        discTime = 0
        for i in range(locations):
            loc = input()
            graph[loc] = []
            visited[loc] = -1
            low[loc] = -1
            father[loc] = ""
        
        routes = int(input())
        for i in range(routes):
            a, b = list(stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        ap()

        print(f"City map #{count}: {len(apNodes)} camera(s) found")
        for l in sorted(apNodes):
            print(l)
        
        locations = int(input())
        if locations != 0:
            print()

        count += 1

main()