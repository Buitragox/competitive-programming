from sys import stdin
from collections import deque

MAX = 10000
adj = [[] for i in range(MAX)]
inc = [0 for i in range(MAX)]

def kahnAlgorithm(n):
    topo = []
    vis = 0
    cola = deque()
    for i in range(n):
        if inc[i] == 0:
            cola.append(i)

    while len(cola) != 0:
        node = cola.popleft()
        topo.append(node)

        for i in range(len(adj[node])):
            adjNode = adj[node][i]
            inc[adjNode] -= 1
            if inc[adjNode] == 0:
                cola.append(adjNode)
        vis += 1

    if vis != n:
        print("Hay un ciclo")
    else:
        for i in range(n):
            print(topo[i], end = ' ')
        print()

def main():
    n, m = list(map(int, stdin.readline().split()))

    for i in range(n):
        vals = list(map(int, stdin.readline().split()))
        node = vals[0]
        for j in range(node):
            adjNode = vals[j + 1]
            adj[i].append(adjNode)
            inc[adjNode] += 1

    print("Grafo")
    for i in range(n):
        print("Nodo %d:" % i)
        for j in range(len(adj[i])):
            print(adj[i][j], end = ' ')
        print()

    print("Ordenamiento Topológico:")
    kahnAlgorithm(n)

main()

    
    
