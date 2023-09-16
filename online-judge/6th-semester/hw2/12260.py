# Jhoan Manuel Buitrago Chavez
# 8953846

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)

start = None
values = []
mem = None

def pairmax(p1, p2):
    ans = None
    if p1[1] > p2[1]:
        ans = p1
    elif p2[1] > p1[1]:
        ans = p2
    else:
        ans = p1 if p1[0] < p2[0] else p2
    return ans


def pairsum(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


def available(n):
    jan = n // 2
    if start == "Jan" and (n % 2 != 0):
        jan += 1 
    return jan
    
def knapsack(n, m):
    global start
    ans = None
    if n == 0 or m == 0 or available(n) < m:
        ans = (0, 0)
    else:
        p1 = pairsum(knapsack(n - 1, m - 1), values[n - 1])
        p2 = knapsack(n - 1,m)
        #print(p1, p2)
        ans = pairmax(p1, p2)
    #print(n, m, available(n),ans)
    return ans

def knapsackMem(n, m):
    global start
    ans = None
    key = (n, m)
    if key in mem:
        ans = mem[key]
    else:   
        if n == 0 or m == 0 or available(n) < m:
            ans = (0, 0)
        else:
            p1 = pairsum(knapsackMem(n - 1, m - 1), values[n - 1])
            p2 = knapsackMem(n - 1, m)
            #print(p1, p2)
            ans = pairmax(p1, p2)
        mem[key] = ans
        #print(n, m, available(n),ans)
    return ans

    
def main():
    global start, values, mem
    cases = int(stdin.readline())
    for _ in range(cases):
        n = int(stdin.readline())
        start = stdin.readline().rstrip()
        values = []
        total_petra = 0
        for _ in range(n):
            p, j = map(int, stdin.readline().split())
            values.append((p, j))
            total_petra += p
            
        values.sort(key=lambda x: (-x[0], x[1]))
        mem = {}
        ans = knapsackMem(n, available(n))
        print(total_petra - ans[0], ans[1])
        cases -= 1

main()