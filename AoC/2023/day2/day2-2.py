"""
Jhoan Buitrago
01/12/2023 dd/mm/yyyy

https://adventofcode.com/2023/day/2

For each game, check that the amount of cubes doesn't exceed the max amount
for the cubes color.

Sum the game id of all games that do not break this rule.
"""

from sys import stdin
from functools import reduce

def main():
    total = 0
    line = stdin.readline()
    game_id = 1
    while line != "":
        line.strip()
        _, sets = line.split(":")
        sets = sets.split(";")

        max_value = {"red": 0, "green": 0, "blue": 0}

        for s in sets:
            cubes_data = s.split(",")
            for c in cubes_data:
                amount, color = c.strip().split(" ")
                max_value[color] = max(max_value[color], int(amount))
        
        tmp = reduce(lambda x, y: x * y, max_value.values())
        total += tmp
        
        line = stdin.readline()
        game_id += 1

    print(total)

        
if __name__ == "__main__":
    main()