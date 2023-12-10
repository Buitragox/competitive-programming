from math import floor, ceil, sqrt
import re
from sys import stdin

def find_range(T: int, R: int) -> tuple[int, int]:
    root = sqrt((T**2 - 4*R))
    sol1 = floor((T - root) / 2) + 1
    sol2 = ceil((T + root) / 2) - 1
    return sol1, sol2


def solve(times: list[int], records: list[int]) -> int:
    total = 1

    for T, R in zip(times, records):
        sol1, sol2 = find_range(T, R)
        range_sol = sol2 - sol1 + 1
        print(sol1, sol2, range_sol)
        total *= range_sol

    return total


def main():
    _, *times_str = re.split(r"\s+", stdin.readline().strip())
    times = list(map(int, times_str))

    _, *records_str = re.split(r"\s+", stdin.readline().strip())
    records = list(map(int, records_str))

    print(solve(times, records))
    

if __name__ == "__main__":
    main()