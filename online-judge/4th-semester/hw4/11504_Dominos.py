from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10000000)

visited = [False for _ in range(100002)]
n = 0
count = 0
graph = []
topo = []

def topoSortAux(node):
    global topo, visited
    visited[node] = True
    for i in range(len(graph[node])):
        adjNode = graph[node][i]
        if not visited[adjNode]:
            topoSortAux(adjNode)
    topo.append(node)

def topoSort():
    global visited
    for i in range(n):
        visited[i] = False
    
    for i in range(n):
        if not visited[i]:
            topoSortAux(i)

def dfsAux(node):
    visited[node] = True
    for i in range(len(graph[node])):
        adjNode = graph[node][i]
        if not visited[adjNode]:
            dfsAux(adjNode)

def dfs():
    global count, topo, visited
    for i in range(n):
        visited[i] = False
    
    topo.reverse()
    for node in topo:
        if not visited[node]:
            dfsAux(node)
            count += 1

def main():
    global n, count, graph
    cases = int(input())
    while cases:
        n, m = list(map(int, stdin.readline().split()))
        count = 0
        topo = []
        graph = [[] for _ in range(n)]
        for i in range(m):
            node, adjNode = list(map(int, stdin.readline().split()))
            graph[node - 1].append(adjNode - 1)
        
        topoSort()
        dfs()
        print(count)
        cases -= 1

main()