from math import floor, ceil, sqrt, log10
import re
from sys import stdin
from functools import reduce

def find_range(T: int, R: int) -> tuple[int, int]:
    """
    The traveled distance function is f(t) = t * (T - t) = -t^2 + T*t
    where T is the total time for the competition
    and t is the time spent pressing the button.

    We want to find the two answers for time t where
    R = -t^2 + T*t
    t^2 - T*t + R = 0
    so we can know the range of numbers that would break the record

    t1 = (T - sqrt((-T)^2 - 4(1)(R))) / 2
    t2 = (T + sqrt((-T)^2 - 4(1)(R))) / 2

    We return the leftmost and rightmost integer in the range that break the record
    """
    root = sqrt((T**2 - 4*R))
    sol1 = floor((T - root) / 2) + 1 # we apply floor() + 1 to get next integer that breaks the record
    sol2 = ceil((T + root) / 2) - 1  # we apply ceil() - 1 to get next integer that breaks the record
    return sol1, sol2


def digits(num: int) -> int:
    return floor(log10(num)) + 1


def main():
    _, *times_str = re.split(r"\s+", stdin.readline().strip())
    time = int(reduce(lambda x,y: x+y, times_str))

    _, *records_str = re.split(r"\s+", stdin.readline().strip())
    record = int(reduce(lambda x,y: x+y, records_str))

    sol1, sol2 = find_range(time, record)
    range_sol = sol2 - sol1 + 1

    print(range_sol)
    

if __name__ == "__main__":
    main()