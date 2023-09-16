# Jhoan Manuel Buitrago Chavez
# 8953846
# 01/03/2022
# dd/mm/yyyy

from sys import stdin

N = 0
table = []

def moves(r, c):

    ans = None
    if r >= N:
        ans = [c, c+1]
    else:
        ans = []
        if c != 0:
            ans.append(c-1)
        if c != r:
            ans.append(c)
    return ans

def solve_aux(r, c, x, memo):
    #global table
    ans = False
    key = (r, c, x)
    if key in memo:
        ans = memo[key]
    else:
        if r == 0: #Si es la última posición
            ans = abs(table[0][0]) == abs(x)
        else:
            ans = False
            n = 0
            movelist = moves(r, c)
            #print(r, c)
            #print(table)
            t = table[r][c]
            
            #print(movelist)
            while not ans and n<len(movelist):
                newC = movelist[n]
                ans = solve_aux(r - 1, newC, x + t, memo) or \
                      solve_aux(r - 1, newC, x - t, memo)
                n += 1
        memo[key] = ans
                
    return ans

def solve():
    n = 0
    found = False
    memo = {}
    start = 2 * N - 2
    while not found:
        found = solve_aux(start, 0, n, memo) 
        n += 1
    return n - 1

def main():
    global N, table
    n = int(stdin.readline())
    while n != 0:
        table = []
        for i in range(2*n - 1):
            row = list(map(int, stdin.readline().split()))
            table.append(row)

        N = n
        ans = solve()
        print(ans)
        n = int(stdin.readline()) 

main()