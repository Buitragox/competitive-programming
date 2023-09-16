from sys import stdin
from sys import setrecursionlimit 
setrecursionlimit(10000)

processed = []
dEdges = set()
graph = []
visited = []
low = []
father = []
discTime = 0

def bridgesAux(node):
    global discTime, visited, father, low, dEdges
    discTime += 1
    visited[node] = discTime
    low[node] = discTime
    
    for i in range(len(graph[node])):
        adjNode = graph[node][i]
        pair = (min(node, adjNode), max(node, adjNode))

        if pair not in processed:
            processed.append(pair)

            if visited[adjNode] == -1:
                father[adjNode] = node
                bridgesAux(adjNode)
                low[node] = min(low[node], low[adjNode])

                #Verificar si es un puente
                if low[adjNode] > visited[node]:
                    #añado el contrario
                    dEdges.add((adjNode, node))

            #back-edge
            elif adjNode != father[node]:
                low[node] = min(low[node], visited[adjNode])
            
            #añado el normal
            dEdges.add((node, adjNode))
   
def bridges():
    for i in range(len(graph)):
        if visited[i] == -1:
            bridgesAux(i)


def main():
    global graph, visited, low, father, discTime, processed, dEdges
    count = 1
    n, m = list(map(int, stdin.readline().split()))
    while(n != 0):
        processed = []
        dEdges = set()
        graph = [[] for _ in range(n)]
        visited = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        father = [-1 for _ in range(n)]
        discTime = 0

        for i in range(m):
            a, b = list(map(int, stdin.readline().split()))
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        bridges()

        print(count)
        print()
        for p in sorted(dEdges):
            print(p[0] + 1, p[1] + 1)
        print("#")
        n, m = list(map(int, stdin.readline().split()))

        count += 1
        

main()