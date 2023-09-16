# Jhoan Manuel Buitrago Chavez
# 8953846

from sys import stdin

MAXN = 61 # 0 - 60

mem = [[None for _ in range(MAXN)] for _ in range(MAXN)]
back = None

def trib(n:int):
    ans = 0
    if n > 1:
        if mem[n][back] != None:
            ans = mem[n][back]
            #ans = mem[n]
        else:   
            for i in range(1, back + 1):
                ans += trib(n - i) + 1 #Plus one for every function call
            #mem[n] = ans
            mem[n][back] = ans
    return ans

def main():
    global mem, back
    cases = 1
    n, back = map(int, stdin.readline().split())
    while n <= 60:
        #mem = {}
        ans = trib(n) + 1 #Plus one to count first function call
        print(f"Case {cases}: {ans}")
        cases += 1
        n, back = map(int, stdin.readline().split())

main()
