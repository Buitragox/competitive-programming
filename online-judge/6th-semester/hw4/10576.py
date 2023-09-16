# Jhoan Manuel Buitrago Chavez
# 8953846
# 11/04/2022
# dd/mm/yyyy

# https://onlinejudge.org/external/105/10576.pdf

from sys import stdin

M = 12 #months
G = 5 #size of consecutive months

res = []
max_bens = 0
max_defs = 0

def check_valid(n: int, reports: list) -> bool:
    valid = True
    sum_group = 0
    for i in range(n, n - G, -1):
        sum_group += reports[i]

    if sum_group > 0:
        valid = False
    
    return valid


def solve(n: int, s: int, d: int, reports: list, defs: int, bens: int) -> bool:
    global res
    found = False #if false, continue searching
    if n == M: #Found solution, which must be maximum
        res = list(reports)
        found = True
        
    elif n < M:
        #need at least 5 positions set to check groups

        #first sets are without group check
        if n < G - 1:
            if (bens + 1) <= max_bens:
                found = solve(n+1, s, d, reports, defs, bens + 1)

            reports[n] = -d 
            if not(found) and (defs + 1) <= max_defs:
                found = solve(n+1, s, d, reports, defs + 1, bens)

        #if n is at least 5, check groups
        else:
            if check_valid(n, reports) and (bens + 1) <= max_bens:
                found = solve(n+1, s, d, reports, defs, bens + 1)
            
            reports[n] = -d
            if not(found) and check_valid(n, reports) and (defs + 1) <= max_defs:
                found = solve(n+1, s, d, reports, defs + 1, bens)
        
        reports[n] = s
        
    return found
            
    
def main():
    global max_bens, max_defs
    line = stdin.readline()
    
    while line != "":
        s, d = map(int, line.split())
        reports = [s] * M

        defs = 0
        bens = M
        #Check max amount of defs
        while bens * s >= defs * d:
            defs += 1
            bens -= 1

        #Set maximum amounts of deficits and benefits
        max_defs = defs - 1
        max_bens = 10

        found = False
        #Every solution must have at least 2 deficits
        if max_defs >= 2:
            found = solve(0, s, d, reports, 0, 0)

        if not found:
            print("Deficit")
        else:
            print(sum(res))
        print(res)

        line = stdin.readline()
    

main()