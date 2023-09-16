from heapq import heappop, heappush
from sys import stdin

INF = float('inf') # math.inf

def dijkstra(G, s):
    d, p = [INF for i in range(len(G))], [-1 for i in range(len(G))]
    d[s] = 0
    heap = [(0, s)]

    while len(heap) != 0:
        costo, node = heappop(heap)
        if costo == d[node]:
            for adjNode, weight in G[node]:
                if d[adjNode] > d[node] + weight:
                    d[adjNode], p[adjNode] = d[node] + weight, node
                    heappush(heap, (d[adjNode], adjNode))
    return d, p

def main():
    cases = int(input())
    while cases:
        n, m, start, end, money = map(int, stdin.readline().split())
        start -= 1
        end -= 1
        graph = [[] for _ in range(n)]
        revGraph = [[] for _ in range(n)]
        for i in range(m):
            node, adjNode, weight = map(int, stdin.readline().split())
            graph[node - 1].append((adjNode - 1, weight))
            revGraph[adjNode - 1].append((node - 1, weight))
        
        dist, pred = dijkstra(graph, start)
        revDist, revPred = dijkstra(revGraph, end)
        #print(dist)
        #print(revDist)

        if dist[end] <= money:
            maxValue = 0
            for i in range(n):
                for adj, w in graph[i]:
                    value = dist[i] + revDist[adj] + w
                    if value <= money and maxValue < w:
                        maxValue = w
            print(maxValue)
        else:
            print("-1")
    
        cases -= 1

main()