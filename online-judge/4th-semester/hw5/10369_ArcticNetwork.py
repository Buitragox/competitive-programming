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
        return f"({self.node}, {self.adj}, {self.weight})"

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

def kruskal(n, disSet: DisjointSet, edges: list, sat):
    global total
    #mst = []
    forests = n

    for i in range(n):
        disSet.makeSet(i)
    
    lastEdge = Edge()
    for edge in sorted(edges):
        node = edge.node
        adj = edge.adj

        if disSet.findSet(node) != disSet.findSet(adj):
            #mst.append(edge)
            disSet.unionSet(node, adj)
            forests -= 1
        
        if forests == sat:
            lastEdge = edge
            break

    # Último edge usado en orden ascendente
    print("%.2f" % lastEdge.weight)
    
    #return mst

def main():
    cases = int(input())
    while cases:
        
        sat, outposts = map(int, stdin.readline().split())
        edges = []
        coords = []
        for i in range(outposts):
            x, y = map(int, stdin.readline().split())
            coords.append((x, y))
        for i in range(outposts):
            for j in range(i, outposts):
                if i != j:
                    insx = (coords[j][0] - coords[i][0]) ** 2
                    insy = (coords[j][1] - coords[i][1]) ** 2
                    distance = (insx + insy) ** (1/2)
                    edges.append(Edge(i, j, distance))
        #print(*edges)
        disSet = DisjointSet(outposts)

        kruskal(outposts, disSet, edges, sat)

        # print("El peso total del arbol del recubrimiento es:", total)
        # print("Aristas:")
        # for i in range(len(mst)):
        #     print(mst[i])

        cases -= 1

main()            