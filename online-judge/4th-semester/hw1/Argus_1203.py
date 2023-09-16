from heapq import heappop, heappush
from sys import stdin

class Query:
    qId = 0
    period = 0
    p = 0
    def __init__(self, newId, newPeriod, newP):
        self.qId = newId
        self.period = newPeriod
        self.p = newP
    
    def __lt__(self, other):
        if self.period != other.period:
            return self.period < other.period
        return self.qId < other.qId
     

def main():
    prioQ = []
    line = stdin.readline()
    while line[0] != "#":
        parts = line.split()
        newQuery = Query(int(parts[1]), int(parts[2]), int(parts[2]))
        heappush(prioQ, newQuery)
        line = stdin.readline()
    
    k = int(stdin.readline())
    for i in range(0, k):
        top = heappop(prioQ)
        print(top.qId)
        top.period += top.p
        heappush(prioQ, top)

main()