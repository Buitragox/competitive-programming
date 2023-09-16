from sys import stdin

class Edge():
    node = 0
    adj = 0
    weight = 0
    def __init__(self, x=0, y=0, w=0):
        self.node = x
        self.adj = y
        self.weight = w

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"({self.node}, {self.adj})"

class DisjointSet():
    parent = []
    rank = []
    def __init__(self, n):
        self.parent = [0 for _ in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def makeSet(self, v):
        self.parent[v] = v
        self.rank[v] = 0
    
    def findSet(self, v):
        ans = None
        if v == self.parent[v]:
            ans = v
        else:
            self.parent[v] = self.findSet(self.parent[v])
            ans = self.parent[v]
        return ans

    def unionSet(self, v, u):
        v = self.findSet(v)
        u = self.findSet(u)

        if v != u:
            if self.rank[v] < self.rank[u]:
                v, u = u, v
            self.parent[u] = v
            if self.rank[v] == self.rank[u]:
                self.rank[v] += 1

count = 1

def kruskal(n, disSet: DisjointSet, edges: list):
    #global total
    mst = []

    for i in range(n):
        disSet.makeSet(i)

    edges.sort(reverse=True)
    for edge in edges:
        node = edge.node
        adj = edge.adj

        if disSet.findSet(node) != disSet.findSet(adj):
            mst.append(edge)
            #total += edge.weight
            disSet.unionSet(node, adj)
    print(f"Case #{count}:", mst[-1].weight)
    
    #return mst

def main():
    global count
    cases = int(input())
    while cases:
        n, m = map(int, stdin.readline().split())
        edges = []
        for i in range(m):
            node, adj, weight = map(int, stdin.readline().split())
            edges.append(Edge(node, adj, weight))
        
        disSet = DisjointSet(n)

        kruskal(n, disSet, edges)
        count += 1
        cases -= 1
main()            