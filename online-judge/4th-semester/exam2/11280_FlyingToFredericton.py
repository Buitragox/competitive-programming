from sys import stdin

INF = float('inf')

def bellmanFordOpt(G: dict, cities: list, Q: list):
    global d, p
    n = len(cities)
    d = {c:INF for c in cities}
    d["Calgary"] = 0

    answers = {x:"No satisfactory flights" for x in Q}
    cities.reverse()
    for i in range(n):
        for u in cities:
            for v, w in G[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
        if d["Fredericton"] != INF and i in Q:
            answers[i] = "Total cost of flight(s) is $" + str(d["Fredericton"])
    

    if d["Fredericton"] != INF:
        for elem in Q:
            if elem >= n:
                answers[elem] = "Total cost of flight(s) is $" + str(d["Fredericton"])
    
    return answers

def main():
    cases = int(input())
    count = 1
    while cases:
        empty = stdin.readline()
        n = int(input())
        cities = []
        graph = {}
        for i in range(n):
            c = input()
            cities.append(c)
            graph[c] = []

        m = int(input())
        for i in range(m):
            a, b, w = stdin.readline().split()
            weight = int(w)
            graph[a].append((b, weight))
        
        Q = list(map(int, stdin.readline().split()))[1:]

        ans = bellmanFordOpt(graph, cities, Q)

        
        print("Scenario #" + str(count))
        for q in Q:
            print(ans[q])

        cases -= 1
        count += 1
        if cases != 0:
            print()

main()