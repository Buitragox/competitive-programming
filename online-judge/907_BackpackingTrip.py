# Jhoan Manuel Buitrago Chavez
# 8953846

from sys import stdin

MAXN = 603

total = [0 for _ in range(MAXN)]
#dist = [0 for _ in range(MAXN)]
N = 0
mem = {}

#total_dist[i] = total distance from start to camp[i]
#total_dist[N + 1] = total distance from start to end

#Solution with DP
def solve(i, sleeps):
    ans = None
    key = (i, sleeps)
    if sleeps == 0: # If cant sleep, finish
        ans = total[N + 1] - total[i]
    elif key in mem: # If there is a solution
        ans = mem[key]
    else:
        ans = float('inf')
        # N+1 - sleeps is the maximum node I can reach without wasting sleeps, 
        # +1 to include inside for
        for u in range(i + 1, N + 1 - sleeps + 1): 
            #print(f"Node {i}\n\t{u}: value {total[u] - total[i]}")
            path = max(solve(u, sleeps - 1), total[u] - total[i])
            ans = min(ans, path)
        mem[key] = ans
    return ans


def main():
    global N, mem
    line = stdin.readline()
    while line != "":
        N, k = map(int, line.split())
        mem = {}

        for i in range(1, N+2):
            #dist[i] = int(stdin.readline())
            total[i] = total[i-1] + int(stdin.readline())

        sleeps = N if k > N else k #max sleeps is N
        print(solve(0, sleeps))
        line = stdin.readline()

main()