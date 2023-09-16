from sys import stdin

adj = []
visitado = []
pushed = 0

def dfs(node):
    global pushed
    visitado[node] = True
    pushed += 1

    for i in range(len(adj[node])):
        adjNode = adj[node][i]
        if not visitado[adjNode]:
            dfs(adjNode)

def main():
    global visitado, adj, pushed
    cases = int(stdin.readline())
    while cases: 
        n, m, l = list(map(int, stdin.readline().split()))
        adj = [[] for _ in range(n)]
        visitado = [False for _ in range(n)]
        for i in range(m):
            x, y = list(map(int, stdin.readline().split()))
            adj[x - 1].append(y - 1)

        pushed = 0
        for j in range(l):
            z = int(stdin.readline()) - 1
            if not visitado[z]:
                dfs(z)
        
        print(pushed)
        cases -= 1

main()
