# Jhoan Manuel Buitrago Chavez
# 8953846
# 12/03/2022
# dd/mm/yyyy

from sys import stdin
from heapq import heappush, heappop


def greedy_agenda(events:list) -> int:
    ans = 0
    last_time = -1
    while len(events) > 0:
        e = heappop(events)
        if e[1] >= last_time:
            ans += 1
            last_time = e[0]
    return ans


def main() -> None:
    events = []
    cases = int(stdin.readline())
    for _ in range(cases):
        s, f = map(int, stdin.readline().split())
        while s > 0 or f > 0:
            heappush(events, (f, s))
            s, f = map(int, stdin.readline().split())
            
        ans = greedy_agenda(events)
        print(ans)

main()