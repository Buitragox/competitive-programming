from sys import stdin
from math import sqrt
from collections import deque


def bfs(u, adj, visitados, distancia):
    cola = deque()
    cola.append(u)
    visitados[u] = True
    distancia[0] = 0
    stop = False
    while len(cola) != 0 and not stop:
        v = cola.popleft()
        w = 0
        for i in range(len(adj[v])):
            w = adj[v][i]
            if not visitados[w]:
                cola.append(w)
                visitados[w] = True
                distancia[w] = distancia[v] + 1

                if w == 1:
                    stop = True
                    break;


def makeAdj(adj, holes, v, m):
    for i in range(len(holes)):
        x1 = holes[i][0]
        y1 = holes[i][1]
        for j in range(len(holes)):
            x2 = holes[j][0]
            y2 = holes[j][1]
            if holes[i] != holes[j]:
                distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                time = distance / v
                if time < m * 60:
                    adj[i].append(j)
            
def main():
    v, m = list(map(int, stdin.readline().split()))
    while v != 0 and m != 0:
        holes = []
        holes.append(tuple(map(float, stdin.readline().split())))
        holes.append(tuple(map(float, stdin.readline().split())))
        line = stdin.readline()
        while line != "" and line != "\n":
            holes.append(tuple(map(float, line.split())))
            line = stdin.readline()

        adj = [[] for _ in range(len(holes))]
        visitado = [False for _ in range(len(holes))]
        distancia = [-1 for _ in range(len(holes))]
        makeAdj(adj, holes, v, m)
        if(len(adj[1]) == 0):
            print("No.")
        else:
            bfs(0, adj, visitado, distancia)
            if distancia[1] == -1:
                print("No.")
            else:
                print(f"Yes, visiting {distancia[1] - 1} other holes.")

        v, m = list(map(int, stdin.readline().split()))

main()