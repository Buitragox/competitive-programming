from sys import stdin
from heapq import heappush
from heapq import heappop

def kahnAlgorithm(inc, adj, beverages):
    topo = []
    vis = 0
    cola = []
    for bev in beverages:
        if inc[bev] == 0:
            index = beverages.index(bev)
            heappush(cola, (index, bev))

    while len(cola) != 0:
        index, node = heappop(cola)
        topo.append(node)

        for i in range(len(adj[node])):
            adjNode = adj[node][i]
            inc[adjNode] -= 1
            if inc[adjNode] == 0:
                index = beverages.index(adjNode)
                heappush(cola, (index, adjNode))
        vis += 1

    return topo
            

def main():
    case = 1
    lineN = stdin.readline() 
    while lineN != "" and lineN != "\n" and lineN != "stop":
        n = int(lineN)
        adj = {}
        inc = {}
        beverages = []
        for i in range(n):
            bev = input()
            beverages.append(bev)
            inc[bev] = 0
            adj[bev] = []
        m = int(stdin.readline())
        for j in range(m):
            bevA, bevB = list(stdin.readline().split())
            inc[bevB] += 1
            adj[bevA].append(bevB)

        topo = kahnAlgorithm(inc, adj, beverages)
        print(f"Case #{case}: Dilbert should drink beverages in this order: ", end="")
        print(*topo, end = ".\n\n")
        case += 1
        input()
        lineN = stdin.readline()

main()

    
    
