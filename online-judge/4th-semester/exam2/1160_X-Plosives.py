from sys import stdin

class Edge():
    node = 0
    adj = 0
    weight = 0
    def __init__(self, x, y):
        self.node = x
        self.adj = y

    def __str__(self):
        return f"({self.node}, {self.adj})"

class DisjointSet():
    parent = []
    rank = []
    def __init__(self, vertices):
        self.parent = vertices.copy()
        self.rank = vertices.copy()
    
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

def kruskal(vertices: dict, disSet: DisjointSet, edges: list):
    refusals = 0

    keys = vertices.keys()
    for k in keys:
        disSet.makeSet(k)

    for edge in edges:
        node = edge.node
        adj = edge.adj
        if disSet.findSet(node) != disSet.findSet(adj):
            disSet.unionSet(node, adj)
        else:
            refusals += 1
    print(refusals)


def main():
    line = stdin.readline()
    while line != "":
        if len(line) > 0 and line != "\n":
            edges = []
            vertices = {}
            while line != "-1" and line != "-1\n":
                node, adj = map(int, line.split())
                node -= 1
                adj -= 1
                edges.append(Edge(node, adj))
                vertices[node] = 0
                vertices[adj] = 0
                line = stdin.readline()
            disSet = DisjointSet(vertices)
            kruskal(vertices, disSet, edges)
        line = stdin.readline()

main()            