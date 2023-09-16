# Jhoan Manuel Buitrago Chavez
# 8953846
# 13/04/2022
# dd/mm/yyyy

# Problem link: https://onlinejudge.org/external/117/11753.pdf

# Solution works but because of the nature of the problem it was not accepted in Python
# ANSI C solution uses same algorithm and is accepted

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)


def solve(left, right, inserts, nums, K):
    ans = None
    if left >= right or inserts > K:
        ans = inserts

    elif nums[left] == nums[right]:
        ans = solve(left + 1, right - 1, inserts, nums, K)

    else:
        #add numbers to the left of nums[left], or the right of nums[right]
        ans = min(solve(left, right - 1, inserts + 1, nums, K), 
                  solve(left + 1, right, inserts + 1, nums, K))

    return ans


def main():
    cases = int(stdin.readline())
    for case in range(1, cases + 1):
        
        N, K = map(int, stdin.readline().split())
        numbers = list(map(int, stdin.readline().split()))

        inserts = solve(0, N - 1, 0, numbers, K)
    
        print(f"Case {case}: ", end = "")
        if inserts > K:
            print("Too difficult")
        elif inserts == 0:
            print("Too easy")
        else:
            print(inserts)


main()