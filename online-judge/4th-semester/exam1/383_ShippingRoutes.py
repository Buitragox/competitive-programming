from sys import stdin
from collections import deque

def bfs(start, end, adj, codeNames):
    visited = {}
    distance = {}
    for code in codeNames:
        visited[code] = False
        distance[code] = -1
    # visited = { wh : False for wh in warehouses}
    # distance = { wh : -1 for wh in warehouses}
    cola = deque()
    cola.append(start)
    visited[start] = True
    distance[start] = 0
    stop = False
    while len(cola) != 0 and not stop:
        node = cola.popleft()
        w = ""
        for i in range(len(adj[node])):
            w = adj[node][i]
            if not visited[w]:
                cola.append(w)
                visited[w] = True
                distance[w] = distance[node] + 1
                if w == end:
                    stop = True
                    break;
    return distance[end]

def main():
    sets = int(input())
    count = 1
    print("SHIPPING ROUTES OUTPUT\n")
    while sets:
        warehouses, legs, requests = list(map(int, stdin.readline().split()))
        codeNames = list(stdin.readline().split())
        adj = { code : [] for code in codeNames}
        for i in range(legs):
            node1, node2 = list(stdin.readline().split())
            adj[node1].append(node2)
            adj[node2].append(node1)
        print(f"DATA SET  {count}\n")
        for i in range(requests):
            size, start, end = list(stdin.readline().split())
            sizeInt = int(size)
            distance = bfs(start, end, adj, codeNames)
            if distance == -1:
                print("NO SHIPMENT POSSIBLE")
            else:
                cost = sizeInt * distance * 100
                print("$" + str(cost))
        count += 1
        print()
        sets -= 1
    print("END OF OUTPUT")


main()