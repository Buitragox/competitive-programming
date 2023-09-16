# Jhoan Manuel Buitrago Chavez
# 8953846
# 11/04/2022
# dd/mm/yyyy

from sys import stdin

letters = ['A', 'C', 'G', 'T']
N = 0

def solve(n: int, changes: int, seq: list, ans: set):
    if n == N and changes == 0:
        ans.add("".join(seq))
    elif changes <= N - n:

        #Change nothing
        solve(n + 1, changes, seq, ans)

        #Still have remaining changes
        if changes > 0:
            tmp = seq[n]
            for l in letters:
                seq[n] = l
                solve(n + 1, changes - 1, seq, ans)
            seq[n] = tmp


def main():
    global res, N
    cases = int(stdin.readline())
    for _ in range(cases):
        N, K = map(int, stdin.readline().split())
        seq = list(stdin.readline().rstrip())
        ans = set()
        solve(0, K, seq, ans)

        print(len(ans))
        for s in sorted(ans):
            print(s)

main()