# Jhoan Manuel Buitrago Chavez
# 8953846
# Towards Zero
# https://onlinejudge.org/external/110/11002.pdf
# 01/03/2022 dd/mm/yyyy

from sys import stdin

# Get possible moves from (r, c)
def moves(r:int, c:int, N:int, table:list) -> list:
    ans = []
    if r >= N:
        ans.append(c)
        ans.append(c + 1)
    else:
        if c != 0:
            ans.append(c-1)
        if c != r:
            ans.append(c)
    return ans

def solve_aux(r:int, c:int, x:int, memo:dict, table:list, N:int) -> bool:
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
            movelist = moves(r, c, N, table)
            t = table[r][c] 
            while not ans and n<len(movelist):
                newC = movelist[n]
                ans = solve_aux(r - 1, newC, x + t, memo, table, N) or \
                      solve_aux(r - 1, newC, x - t, memo, table, N)

                n += 1
        memo[key] = ans
                
    return ans

# Try to guess the nearest possible value to 0
def solve(table:list, N:int) -> int:
    n = 0
    found = False
    memo = {}
    start = N*2-2
    while not found:
        found = solve_aux(start, 0, n, memo, table, N) #or \
                #solve_aux(start, 0, -n, memo, table, N)
        n += 1
    return n - 1

def main():
    n = int(stdin.readline())
    while n != 0:
        table = []
        for i in range(2*n - 1):
            row = list(map(int, stdin.readline().split()))
            table.append(row)
        
        ans = solve(table, n)
        print(ans)
        n = int(stdin.readline()) 

main()
