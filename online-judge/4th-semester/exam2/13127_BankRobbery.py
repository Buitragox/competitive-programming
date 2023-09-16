from heapq import heappop, heappush
from sys import stdin

INF = float('inf') # math.inf

def dijkstra(G: list, s: list):
    """G is a graph representation in adjacency list format with vertices
       in the set { 0, ..., |V|-1 } and source s is a vertex in G"""
    # dist[u] : "minimum distance detected from source to u
    d = [INF for _ in range(len(G))] 
    #p = [-1 for _ in range(len(G))]
    heap = []
    for station in s:
        d[station] = 0
        heappush(heap, (0, station))

    while len(heap) != 0:
        costo, u = heappop(heap)
        if costo == d[u]:
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    #p[v] = u
                    heappush(heap, (d[v], v))
    return d

def main():
    line = stdin.readline()
    while line != "" and line != "\n":
        #print(line)
        sites, roads, banks, pstations = map(int, line.split())
        graph = [[] for i in range(sites)]

        for i in range(roads):
            a, b, w = map(int, stdin.readline().split())
            graph[a].append((b, w))
            graph[b].append((a, w))

        bankList = sorted(list(map(int, stdin.readline().split())))

        if pstations != 0: 
            policeList = list(map(int, stdin.readline().split()))

            dist = dijkstra(graph, policeList)

            largest = max([dist[bank] for bank in bankList])
            maxList = []
            
            for bank in bankList:
                if dist[bank] == largest:
                    maxList.append(bank)
            
            print(len(maxList), largest if largest != INF else "*")
            print(*maxList)
        else:
            print(len(bankList), "*")
            print(*bankList)

        line = stdin.readline()
        
main()